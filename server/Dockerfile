FROM python:2.7.14-alpine
RUN apk update && apk add --virtual deps gcc python-dev musl-dev && apk add postgresql-dev

ENV PYTHONUNBUFFERED 1
ENV APP_CODE /src

RUN mkdir $APP_CODE
ADD . $APP_CODE

RUN pip install -r $APP_CODE/requirements.txt
RUN apk del deps

WORKDIR $APP_CODE
