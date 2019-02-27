from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, BooleanField, SelectField, TextAreaField
from wtforms.widgets import TextArea
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError
from flask_wtf.file import FileField, FileAllowed
import re

from database.models import Database

class DatabaseForm(Form):
    sa = StringField('Solution Architect', [validators.DataRequired()])
    now = StringField('Time Stamp', [validators.DataRequired()])
    num = StringField('Number', [validators.DataRequired()])
    message = StringField('Entry Body', [validators.DataRequired()], render_kw={"rows": 5, "cols": 65})
    concern = StringField('Concerns/Issues', [validators.DataRequired()], render_kw={"rows": 5, "cols": 65})
