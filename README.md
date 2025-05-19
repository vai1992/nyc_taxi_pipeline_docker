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
git clone https://github.com/vai1992/rill_coding_challenge.git
cd rill-coding-challenge

# Start Docker Container
docker-compose up --build

In another terminal
curl 
then rill start

start 