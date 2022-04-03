FROM python:3.10-slim

WORKDIR /usr/src/django/

COPY django/ /usr/src/django/

RUN apt-get -y update \
    && apt-get install -y gcc libpq-dev \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install
