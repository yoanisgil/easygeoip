import socket

import geoip2.database
from sqlalchemy import func

from flask import jsonify, render_template

from easygeoip import app
from easygeoip.models import TzWorld


def get_time_zone(longitude, latitude):
    time_zone = 'Unknown'

    tz_world = TzWorld.query.filter(func.ST_Contains(TzWorld.geom, 'POINT (%s %s)' % (longitude, latitude))).first()

    if tz_world:
        time_zone = tz_world.tzid

    return time_zone


def to_ip(target):
    try:
        socket.inet_aton(target)
        return target
    except socket.error:
        result = socket.gethostbyname(target)

        return result

@app.route('/<target>')
def city_details(target):
    api_response = {}

    try:
        ip = to_ip(target)

        reader = geoip2.database.Reader(app.config.get('MAXMIND_CITY_PATH'))
        response = reader.city(ip)

        raw_response = response.raw

        if 'time_zone' not in raw_response['location']:
            raw_response['location']['time_zone'] = get_time_zone(raw_response['location']['longitude'],
                                                                  raw_response['location']['latitude'])

        api_response['data'] = raw_response
    except Exception, e:
        api_response['error'] = repr(e)

    return jsonify(api_response)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
