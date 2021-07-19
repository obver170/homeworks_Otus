FROM python:3.9-buster


WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY ./ping_pong/pyproject.toml
COPY ./ping_pong/poetry.lock

RUN poetry install

