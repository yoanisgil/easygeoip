__author__ = 'Yoanis Gil'

import os
import gzip
import shutil
import requests
from urlparse import urlparse

from flask.ext.script import Manager

import easygeoip
from easygeoip.config import ConfigProvider

app = easygeoip.create_application()
manager = Manager(app)

config = ConfigProvider.get_config()


def update_maxmind_file(url):
    db_name = urlparse(url).path.split('/')[-1]
    db_path = os.path.join(config.MAXMIND_ROOT, db_name)

    if os.path.exists(db_path):
        os.unlink(db_path)

    r = requests.get(url, stream=True)

    if r.status_code == 200:
        with open(db_path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

    uncompressed_file_path = db_path.split('.gz')[0]
    gzip_file = gzip.open(db_path)

    with open(uncompressed_file_path, 'w+') as f:
        f.write(gzip_file.read())

    gzip_file.close()

    os.unlink(db_path)


@manager.command
def update_maxmind_city_db():
    """
    Download and uncompress maxmind city database.
    :return:
    """
    if not os.path.exists(config.MAXMIND_ROOT):
        os.makedirs(config.MAXMIND_ROOT)

    update_maxmind_file(config.MAXMIND_CITY_DB_URL)


if __name__ == '__main__':
    manager.run()
