#vim:set ft=dockerfile:
FROM ubuntu 
MAINTAINER Yoanis Gil<gil.yoanis@gmail.com>

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive \
     apt-get -y install python python-dev python-pip libpq-dev && \
     rm -rf /var/lib/apt/lists/*

# Create deployment directory
RUN mkdir -p /webapp/

# Make deployment directory the current working directory
WORKDIR /webapp

# Add the application
ADD . /webapp

RUN pip install -r requirements.txt

EXPOSE 5000

RUN python cli.py update_maxmind_city_db 
RUN python cli.py update_maxmind_country_db

CMD ["python", "/webapp/easygeoip.py"]

