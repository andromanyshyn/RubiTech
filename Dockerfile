FROM python:3.10

WORKDIR /django_app

COPY . .

RUN pip install -r requirements.txt

