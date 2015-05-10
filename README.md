#easygeoip

This is a thing layer on top of MaxMind's GeoIP databases (version 2 of Country and City databases).
It enhances these databases by using the [tzworld](http://efele.net/maps/tz/world/) shapefiles to 
provide time zone information when not available.
 
#Usage

- Clone this repo
- Configure your PostgresSQL database with the tzworld shapefiles information. There is already
a [docker image](https://registry.hub.docker.com/u/yoanisgil/tzworld/) so you just can pull and 
launch.
- Edit easygeoip/config.py to point to your PostgreSQL instance
- Launch the application with: python easygeoip.py

You can now visit http://localhost:5000/8.8.8.8.8 or more generally http://localhost:5000/ip_address_here

# Docker compose

There is already a [docker image](https://registry.hub.docker.com/u/yoanisgil/easygeoip/) for launching the 
API/Service. Moreover there is already support for docker compose, so after you clone the repo, and provided
that you have already installed docker, you just need to run:

- docker-compose up

and then visit http://localhost:5000/4.4.4.4

# Todo:

- Add support for various format (XML, YAML ...)



