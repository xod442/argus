from mongoengine import signals
from flask import url_for
import os

from application import db
from utilities.common import utc_now_ts as now

class Vendor(db.Document):
    vend = db.StringField(db_field="c",required=True, Uniqe=True)
