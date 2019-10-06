FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV ENV prod

RUN mkdir /django-docker

WORKDIR /django-docker

ADD requirements.txt /django-docker/

RUN pip install -r requirements.txt

ADD . /django-docker/

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT ["sh", "./docker-entrypoint.sh"]