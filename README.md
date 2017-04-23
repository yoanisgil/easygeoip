#easygeoip

This is a thing layer on top of MaxMind's GeoIP databases (version 2 of the city databases).
It enhances the city database by using the [tzworld](http://efele.net/maps/tz/world/) shapefiles to 
provide time zone information when not available.
 
# Running the API/Website 

    - docker-compose up

and then visit http://localhost:5000/

# Todo:

- Add support for various format (XML, YAML ...)



