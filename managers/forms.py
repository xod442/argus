from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.widgets import TextArea
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError
from flask_wtf.file import FileField, FileAllowed
import re

from links.models import Links

class LinksForm(Form):
    l_id = StringField('Id', [validators.DataRequired()])
    project = StringField('Project', [validators.DataRequired()])
    sa = StringField('S-ASN', [validators.DataRequired()])
    ss = StringField('S-Switch', [validators.DataRequired()])
    sp = StringField('S-Port', [validators.DataRequired()])
    sip = StringField('S-IP addr', [validators.DataRequired()])
    sm = StringField('S-IP mask', [validators.DataRequired()])
    sn = StringField('S-IP Network', [validators.DataRequired()])
    la = StringField('L-ASN', [validators.DataRequired()])
    ls = StringField('L-Switch', [validators.DataRequired()])
    lp = StringField('L-Port', [validators.DataRequired()])
    lip = StringField('L-IP addr', [validators.DataRequired()])
    lm = StringField('L-IP mask', [validators.DataRequired()])
    ln = StringField('L-IP Network', [validators.DataRequired()])
