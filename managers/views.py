
'''
 2016 wookieware.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


__author__ = "@netwookie"
__credits__ = ["Rick Kauffman"]
__license__ = "Apache2"
__version__ = "1.0.0"
__maintainer__ = "Rick Kauffman"
__email__ = "rick@rickkauffman.com"
__status__ = "Prototype"

Flask script that manages ansible variables for Arista Switches
'''
from flask import Blueprint, render_template, request, redirect, session, url_for, abort, flash
import os
from werkzeug import secure_filename
from mongoengine import Q
import datetime
from database.models import Database
from database.forms import DatabaseForm
from database.temp import Temp
from database.number import Number

managers_app = Blueprint('managers_app', __name__)


@managers_app.route('/listentryx', methods=('GET', 'POST'))
def listentryx():
    '''
    List all entries from the database by SA

    '''
    entries = []
    for e in Database.objects():
        entries.append(e)
    return render_template('managers/listentryx.html', entries=entries)

@managers_app.route('/bulk', methods=('GET', 'POST'))
def bulk():
    '''
    List all entries from the database by SA

    '''
    counter = 0
    cr ='\n'
    switch = Switches.query.all()
    f = open(os.path.join(APP_STATIC, 'switchdb.csv'), 'w')
    while (counter < len(switch)):
        line = switch[counter].mac+','+switch[counter].sysname+','+switch[counter].mgmt_ip+','+ \
            switch[counter].mgmt_sub+','+switch[counter].gateway+','+switch[counter].fanDirection \
                +','+switch[counter].localuser+','+switch[counter].passwd+','+  \
                    switch[counter].tftpserver+','+switch[counter].rolex
        f.write(line)
        counter = counter + 1
    f.close()
    flash('Datbase dumped to file /static/switchdb.csv')
    return render_template('dbdump.html')

@managers_app.route('/name', methods=('GET', 'POST'))
def name():
    '''
    List all entries from the database by SA

    '''
    entries = []
    for e in Database.objects():
        entries.append(e)
    return render_template('managers/listentryx.html', entries=entries)
