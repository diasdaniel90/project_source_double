FROM python:3.9.16-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python3 -m pip install --upgrade cython
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

#RUN python3 manage.py makemigrations
#RUN	python3 manage.py migrate


ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV NAME source_double