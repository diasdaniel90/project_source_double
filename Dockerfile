FROM python:3.9-alpine

RUN mkdir /app
WORKDIR /app

RUN apk add --update mariadb-dev
RUN apk add --no-cache \
            --virtual \
            .build-deps \
            python3-dev \
            build-base \
            linux-headers \
            gcc

#RUN mkdir /app
WORKDIR /app

RUN python3 -m pip install --upgrade cython
RUN ls
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

#RUN python3 manage.py makemigrations
#RUN	python3 manage.py migrate


ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV NAME source_double