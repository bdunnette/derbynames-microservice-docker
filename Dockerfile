# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
LABEL maintainer="Brian Dunnette <brian@dunnette.us>" \
    org.opencontainers.image.authors="Brian Dunnette <brian@dunnette.us>" \
    org.opencontainers.image.source="https://github.com/bdunnette/derbynames-microservice-docker"

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
