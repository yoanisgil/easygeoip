import geoip2.database
from flask import jsonify
from easygeoip import app
from easygeoip.models import TzWorld
from sqlalchemy import func


def get_time_zone(longitude, latitude):
    time_zone = 'Unknown'

    tz_world = TzWorld.query.filter(func.ST_Contains(TzWorld.geom, 'POINT (%s %s)' % (longitude, latitude))).first()

    if tz_world:
        time_zone = tz_world.tzid

    return time_zone


@app.route('/<ip>')
def city_details(ip):
    reader = geoip2.database.Reader(app.config.get('MAXMIND_CITY_PATH'))
    response = reader.city(ip)

    raw_response = response.raw

    if 'time_zone' not in raw_response['location']:
        raw_response['location']['time_zone'] = get_time_zone(raw_response['location']['longitude'],
                                                              raw_response['location']['latitude'])

    return jsonify(response.raw)


if __name__ == '__main__':
    app.run()
