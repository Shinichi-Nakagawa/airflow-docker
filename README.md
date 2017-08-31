# airflow-docker 
[![Docker Build Status](https://img.shields.io/docker/build/shinyorke/airflow.svg)]()

[![Docker Hub](https://img.shields.io/badge/docker-ready-blue.svg)](https://hub.docker.com/r/shinyorke/airflow/)
[![Docker Pulls](https://img.shields.io/docker/pulls/shinyorke/airflow.svg)]()
[![Docker Stars](https://img.shields.io/docker/stars/shinyorke/airflow.svg)]()

This repository contains **Dockerfile** of [apache-airflow](https://github.com/apache/incubator-airflow) for [Docker](https://www.docker.com/)'s [automated build](https://registry.hub.docker.com/u/shinyorke/airflow/) published to the public [Docker Hub Registry](https://registry.hub.docker.com/).

## Informations

* Based on Python (3.6-stretch) official Image [python:3.6-stretch](https://hub.docker.com/_/python/) 
* Install [Docker](https://www.docker.com/)
* Install [Docker Compose](https://docs.docker.com/compose/install/)
* Following the Airflow release from [Python Package Index](https://pypi.python.org/pypi/apache-airflow)

/!\ If you want to use Airflow using Python 2, use TAG [1.8.1](https://github.com/puckel/docker-airflow/releases/tag/1.8.1)

## Installation

Pull the image from the Docker repository.

        docker pull shinyorke/airflow

## Build


        docker build --rm -t shinyorke/airflow .

## Settings

environments for airflow.cfg 

sample:env_example

```bash
# User & HOME
AIRFLOW_USER=airflow
AIRFLOW_HOME=/usr/local/airflow

# Database(MySQL)
AIRFLOW_DB_CONN=mysql://airflow:password@localhost:3306/airflow

# Database(sqlite)
# AIRFLOW_DB_CONN=sqlite:////usr/local/airflow/airflow.db

# Airflow webserver settings
AIRFLOW_WEB_PROTOCOL=http
AIRFLOW_WEB_HOST=localhost
AIRFLOW_WEB_PORT=8080
AIRFLOW_WEB_WORKERS=4

# Airflow worker settings
AIRFLOW_WORKER=redis
AIRFLOW_WORKER_HOST=redis
AIRFLOW_WORKER_PORT=6379
AIRFLOW_WORKER_DATABASE=0

# Airflow base settings
# SequentialExecutor, LocalExecutor, CeleryExecutor
AIRFLOW_EXECUTOR=SequentialExecutor
AIRFLOW_EXAMPLES=False
AIRFLOW_AUTH=False
SQL_ALCHEMY_POOL_SIZE=5
SQL_ALCHEMY_POOL_RECYCLE=3600

# Application PATH
PYTHONPATH=/usr/local/airflow

```

## Usage

### webserver

        docker run -p 8080:8080 --env-file=./env_example shinyorke/airflow webserver init

### scheduler

        docker run --env-file=./env_example shinyorke/airflow scheduler init

### worker

        docker run --env-file=./env_example shinyorke/airflow worker init

## Sample(docker-compose)

airflow service example

* webserver
* scheduler
* worker
* backend
  * MySQL(airflow db)
  * redis(workder queue)

        docker-compose -f docker-compose-example-db.yml up -d
        docker-compose -f docker-compose-example.yml build
        docker-compose -f docker-compose-example.yml up -d

# Wanna help?

Fork, improve and PR. Sorry m(_ _)m

# Maintainer

Shinichi Nakagawa

* [Github](https://github.com/Shinichi-Nakagawa)
* [@shinyorke(Twitter)](https://twitter.com/shinyorke)
* [Facebook](https://www.facebook.com/shinyorke)