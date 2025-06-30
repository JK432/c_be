# Pull the image from Dockerhub
FROM python:alpine3.19



WORKDIR /captchaapi

# set up python environment variables

ENV PYTHONDOWNWRITEBYTECODE 1
ENV PYTHONNUNBUFFER 1

RUN apk update && \
    apk add --no-cache build-base cmake

# Upgrade pip in a **separate RUN**
RUN pip install --upgrade pip

COPY ./requirements.txt /api/requirements.txt
RUN pip install -r /api/requirements.txt

# copy project
COPY . .
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate
