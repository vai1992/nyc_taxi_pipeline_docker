from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import duckdb
import os
from jinja2 import Template
from airflow.exceptions import AirflowFailException

# Define the function to load data
def load_data(**context):
    # Get the partition and run_type from the context
    partition = context['dag_run'].conf.get('ingestion_time', '2024-01-01-00')
    run_type = context['dag_run'].conf.get('run_type', 'monthly')
    year, mon, day, hour = partition.split('-')

    # Adjust the partition values based on the run_type
    if run_type == 'monthly':
        hour = '00'
        day = '00'
    elif run_type == 'daily':
        hour = '00'

    # Create the directory if it doesn't exist
    os.makedirs("/opt/airflow/warehouse", exist_ok=True)
    con = duckdb.connect("/opt/airflow/warehouse/nyc_taxi.duckdb")
    con.execute("CREATE SCHEMA IF NOT EXISTS nyc")

    # Create the table if it doesn't exist
    with open("sql/create_trips_table.sql.j2") as f:
        template = Template(f.read())
        sql = template.render()
        try:
            con.execute(sql)
        except duckdb.Error as e:
            raise AirflowFailException(f"Failed to execute insert SQL: {e}")
        f.close()

    # Insert data into the table
    with open("sql/insert_into_trips_main_table.sql.j2") as f:
        template = Template(f.read())
        sql = template.render(
            hour = hour,
            day = day,
            month = mon,
            year = year,
            run_type = run_type,
        )
        try:
            con.execute(sql)
        except duckdb.Error as e:
            raise AirflowFailException(f"Failed to execute insert SQL: {e}")
        f.close()

default_args = {
    'start_date': datetime(2024, 1, 1),
}

with DAG("nyc_taxi_pipeline",
         default_args=default_args,
         schedule_interval=None,
         catchup=False) as dag:

    t1 = PythonOperator(
        task_id="Complete_Pipeline",
        python_callable=load_data,
        provide_context=True
    )