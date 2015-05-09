__author__ = 'Yoanis Gil'

import os


class ConfigProvider(object):
    _local_config = None

    @classmethod
    def get_config(cls):
        if cls._local_config is None:
            cls._local_config = LocalConfig()

        return cls._local_config


class LocalConfig(object):
    MAXMIND_CITY_DB_URL = 'http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz'
    MAXMIND_COUNTRY_DB_URL = 'http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.mmdb.gz'
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    MAXMIND_ROOT = os.path.join(PROJECT_ROOT, 'data', 'maxmind')
    MAXMIND_CITY_PATH = os.path.join(MAXMIND_ROOT, 'GeoLite2-City.mmdb')
    TZ_WORLD_SQLITE_PATH = os.path.join(PROJECT_ROOT, 'data', 'tz_world', 'tz_world.sqlite')
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mysecretpassword@192.168.59.103:15432/tzworld'

    def __init__(self):
        if 'TZWORLD_NAME' in os.environ:
            ip_address = os.environ['TZWORLD_PORT_5432_TCP_ADDR']
            port = os.environ['TZWORLD_PORT_5432_TCP_PORT']
            self.SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mysecretpassword@%s:%s/tzworld' % (ip_address, port)

        print self.SQLALCHEMY_DATABASE_URI


