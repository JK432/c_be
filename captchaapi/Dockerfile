# Pull the image from Dockerhub
FROM python:alpine3.19


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential cmake && \
    rm -rf /var/lib/apt/lists/* \

WORKDIR /captchaapi

# set up python environment variables

ENV PYTHONDOWNWRITEBYTECODE 1
ENV PYTHONNUNBUFFER 1

# update and  install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /api/requirements.txt
RUN pip install -r /api/requirements.txt

# copy project
COPY . .
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate
