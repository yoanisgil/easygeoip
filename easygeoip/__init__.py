__author__ = 'Yoanis Gil'

from flask import Flask
from easygeoip.config import ConfigProvider
from flask.ext.sqlalchemy import SQLAlchemy

def create_application():
    app = Flask(__name__)

    active_config = ConfigProvider.get_config()
    app.config.from_object(active_config)

    return app


app = create_application()
db = SQLAlchemy(app)


