FROM python:3.10.6-alpine

WORKDIR /usr/src/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/backend
RUN pip install -r requirements.txt

COPY . /usr/src/backend

EXPOSE 8000
CMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']
