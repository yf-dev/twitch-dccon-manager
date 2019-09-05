FROM python:3.7.4-buster

RUN apt-get update && apt-get -y install \
        nginx \
        libpq-dev \
        pipenv \
        supervisor && \
    apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/log/nginx/app
RUN mkdir -p /var/log/uwsgi/app
RUN mkdir -p /var/log/supervisor

RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN pip install virtualenv

COPY flask/Pipfile /var/www/flask/Pipfile
COPY flask/Pipfile.lock /var/www/flask/Pipfile.lock
WORKDIR /var/www/flask
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --dev

EXPOSE 80
EXPOSE 443

CMD ["/usr/bin/supervisord"]
