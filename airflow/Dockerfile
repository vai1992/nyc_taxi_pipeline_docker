FROM apache/airflow:2.7.3-python3.11

USER root

# Install system-level dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    curl \
    wget \
    ca-certificates \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

# Upgrade pip and install Python packages
RUN pip install --upgrade pip setuptools wheel

RUN pip install duckdb pandas pyarrow

RUN pip install Jinja2