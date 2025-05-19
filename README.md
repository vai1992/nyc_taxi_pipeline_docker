# Rill Coding Chanllenge - Data Pipeline

A simple Docker Python package to build and run an Airflow-based data pipeline using NYC Taxi Trip Data.

---

## Features

- Downloads and installs Airflow, DuckDB, Ninja and other dependencies.
- Generates Airflow DAGs using templates.
- Supports daily partitioning and idempotent pipeline logic.
- Supports hourly, daily & monthly ingestion of data.
- Rill BI dashboard.

---

## Technologies Used

- Apache Airflow
- DuckDB
- Jinja2 for templated DAGs
- Rill for Dashboard

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/vai1992/nyc_taxi_pipeline_docker.git
cd nyc_taxi_pipeline_docker

# Start Docker Container
docker-compose up --build

Visit : http://localhost:8080/login/
UserName : admin
Password : admin

# Start Airflow
Unpause the DAG nyc_taxi_pipeline in the Airflow UI
Trigger the DAG manually to run the pipeline.

In another terminal
cd nyc_taxi_pipeline_docker
rill start nycdashboard

# Visit the Rill Dashboard
Visit this for Dashboard http://localhost:9009/files/dashboards/NYC_TAXI_metrics_explore.yaml
Visit this for Canvas http://localhost:9009/files/dashboards/Comparison_Canvas.yaml
```

## Tables Created 

- `nyc.trips`: Contains the yellow taxi trip data.
- `gnyc.trips_error`: Contains the yellow taxi trip data which contains data of some other month which is not of same as import file.