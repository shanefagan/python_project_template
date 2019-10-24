FROM python:3-alpine

COPY . /tmp

WORKDIR /tmp

RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt

RUN pip install -e /tmp
RUN pip install -r /tmp/requirements.txt

COPY bin/app.py bin/app.py
