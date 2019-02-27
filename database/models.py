from mongoengine import signals
from flask import url_for
import os

from application import db
from utilities.common import utc_now_ts as now


class Database(db.Document):
    sa = db.StringField(db_field="sa", required=True)
    message = db.StringField(db_field="m", required=True)
    concern = db.StringField(db_field="w", required=True)
    now = db.StringField(db_field="n", required=True)
    num = db.IntField(db_field="x", required=True)
