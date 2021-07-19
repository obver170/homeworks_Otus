#sudo docker run -p 8000:8000 ping-pong

 
FROM python:3.9-buster


WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY ./ping_pong/pyproject.toml .
COPY ./ping_pong/poetry.lock .

RUN poetry install

COPY ping_pong ./

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]

