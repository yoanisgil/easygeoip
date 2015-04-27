__author__ = 'Yoanis Gil'

from easygeoip import db
from geoalchemy2 import Geometry


class TzWorld(db.Model):
    __tablename__ = 'tz_world'

    gid = db.Column(db.Integer, primary_key=True)
    tzid = db.Column(db.String(30), unique=True)
    geom = db.Column(Geometry('POLYGON'))