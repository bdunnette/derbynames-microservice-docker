# DerbyNames Microservice - Dockerized

A simple container to generate and serve [derby names](https://en.wikipedia.org/wiki/Roller_derby#Derby_names) using [aitextgen](https://docs.aitextgen.io/) and [Django](https://docs.djangoproject.com/).

## Installation

With Docker and Docker Compose installed, you can install the microservice with the following commands:


+ Run database migrations

```bash
    $ docker compose run --rm web python manage.py migrate
```

+ Download RNN model

```bash
    $ docker compose run --rm web python manage.py download_model
```

+ Run containers

```bash
    $ docker compose up -d
```
