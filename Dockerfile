FROM python:2.7-slim 
MAINTAINER Yoanis Gil<gil.yoanis@gmail.com>

RUN mkdir /srv/app
WORKDIR /srv/app

# Install require software and libraries
ADD ./docker/nginx.list /etc/apt/sources.list.d/nginx.list

RUN apt-get update && \
    apt-get -y install curl && \ 
    curl http://nginx.org/keys/nginx_signing.key | apt-key add - && \
    apt-get update && \
    apt-get -y install build-essential libpq-dev nginx supervisor && \
    rm -rf /var/lib/apt/lists/*

ADD ./docker/nginx.conf /etc/nginx/nginx.conf
ADD ./docker/supervisord.conf /etc/supervisor/supervisord.conf
RUN rm /etc/nginx/conf.d/default.conf
ADD ./docker/site.conf /etc/nginx/conf.d/site.conf

# Create nginx temporary folders.
RUN mkdir -p /tmp/nginx /tmp/app/logs && chown -R www-data: /tmp/nginx /tmp/app/logs

# Copy as early as possible so we can cache ...
ADD ./requirements.txt /srv/app/requirements.txt

# Install application dependencies
RUN pip install  --no-cache-dir -r requirements.txt

# Add the application
ADD . /srv/app

# Download Maxmind Database
RUN python cli.py update_maxmind_city_db

# Application entrypoint
CMD ["supervisord", "-u", "www-data", "-n", "-c", "/etc/supervisor/supervisord.conf"]
