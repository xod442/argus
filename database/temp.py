from mongoengine import signals
from flask import url_for
import os

from application import db

class Temp(db.Document):
    sa = db.StringField(db_field="sa", required=True)
