FROM python:2.7-slim 
MAINTAINER Yoanis Gil<gil.yoanis@gmail.com>

# Create the directory where we will copy the application code 
RUN mkdir /srv/app 
# ... and declare it as the default working directory
WORKDIR /srv/app

# Add Nginx repository so that we install a recent version
ADD ./docker/nginx.list /etc/apt/sources.list.d/nginx.list

# Install required software:
# - Supervisor (for running multiple processes)
# - Nginx
# - libpq-dev because we need to install PostgresSQL's binding for Python
RUN apt-get update && \
    apt-get -y install curl && \ 
    curl http://nginx.org/keys/nginx_signing.key | apt-key add - && \
    apt-get update && \
    apt-get -y install build-essential libpq-dev nginx supervisor && \
    rm -rf /var/lib/apt/lists/*

# Add Nginx configuration
ADD ./docker/nginx.conf /etc/nginx/nginx.conf
# Add supervisor which will take care of running Nginx and UWSGI 
ADD ./docker/supervisord.conf /etc/supervisor/supervisord.conf
# Remove the Nginx's default configuration so that it doesn't create conflicts with our app's
RUN rm /etc/nginx/conf.d/default.conf
# Add the Nginx configuration related to the application. Nothing special here, just standard UWSGI configuration
ADD ./docker/site.conf /etc/nginx/conf.d/site.conf

# Because Nginx is not running as root, we need to make sure that we create the folder where the user www-data can read/write from/to.
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
