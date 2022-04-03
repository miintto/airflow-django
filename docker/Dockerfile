FROM python:3.10-slim AS base

ENV AIRFLOW_HOME=/usr/src/airflow

WORKDIR /usr/src/airflow/

COPY pyproject.toml poetry.lock airflow.cfg webserver_config.py /usr/src/airflow/

RUN apt-get -y update \
    && apt-get install -y gcc libpq-dev \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install
