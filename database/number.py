from mongoengine import signals
from flask import url_for
import os

from application import db

class Number(db.Document):
    num = db.IntField(db_field="x", required=True)
