# syntax=docker/dockerfile:1

FROM python:3.10-rc-slim-buster
WORKDIR /carholder

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && apt-get install -y python-pil \
    && apt-get install -y libjpeg-dev zlib1g-dev \
    && apt-get install -y make \
    && apt-get install -y libfreetype6-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
