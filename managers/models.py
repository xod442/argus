from mongoengine import signals
from flask import url_for
import os

from application import db
from utilities.common import utc_now_ts as now


class Links(db.Document):
    l_id = db.IntField(db_field="l_id", required=True, unique=True)
    project = db.StringField(db_field="p", required=True)
    sa = db.IntField(db_field="sa", required=True)
    ss = db.StringField(db_field="ss", required=True)
    sp = db.StringField(db_field="sp", required=True)
    sip = db.StringField(db_field="sip", required=True)
    sm = db.IntField(db_field="sm", required=True)
    sn = db.StringField(db_field="sn", required=True)
    la = db.IntField(db_field="la", required=True)
    ls = db.StringField(db_field="ls", required=True)
    lp = db.StringField(db_field="lp", required=True)
    lip = db.StringField(db_field="lip", required=True)
    lm = db.IntField(db_field="lm", required=True)
    ln = db.StringField(db_field="ln", required=True)
    created = db.IntField(db_field="c", default=now())
