from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, BooleanField, SelectField
from wtforms.widgets import TextArea
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError
from flask_wtf.file import FileField, FileAllowed
import re

from comwarelib.models import Comware

class ComwareForm(Form):
    role = StringField('Role', [validators.DataRequired()])
    mgmt_ip = StringField('IP Address', [validators.DataRequired()])
    pod = StringField('POD Name', [validators.DataRequired()])
    user = StringField('User', [validators.DataRequired()])
    passwd = PasswordField('Password', [validators.DataRequired()])
    model = SelectField(u'Switch Model', choices=[('12900', '12900'),
                                                 ('7900', '7900'),
                                                 ('5980', '5980'),
                                                 ('5950', '5950'),
                                                 ('5940', '5940')])
    spineAsn = StringField('Spine ASN', [validators.DataRequired()])
    combLeaf = SelectField('Combined Leaf Group ASN', choices=[('No', 'No'),
                                                   ('No', 'Yes')])
