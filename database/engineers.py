from mongoengine import signals
from flask import url_for
import os

from application import db

class Engineers(db.Document):
    name = db.IntField(db_field="n", required=True)
