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
    MAXMIND_ROOT = '/var/lib'
    MAXMIND_CITY_PATH = os.path.join(MAXMIND_ROOT, 'GeoLite2-City.mmdb')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:%s@tz_world_db:5432/tz_world' % os.environ.get('DB_PASSWORD', '')
    DEBUG = bool(int(os.environ.get('DEBUG', 0)))
