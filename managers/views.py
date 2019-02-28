
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
from database.engineers import Engineers

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

@managers_app.route('/download', methods=('GET', 'POST'))
def download():
    '''
    List all entries from the database by SA

    '''
    counter = 0
    cr ='\n'


    if request.method == 'POST':
        # Get desired project
        start = request.form['start']
        start = start.encode('utf-8')
        start = int(start)
        # Set the start back a month to get any weeks that cross month bounry
        if start == 1:
            start = 0
        else:
            start = start - 1

        # Open file for writing
        f = open('/opt/argus/static/sa_activities.csv', 'w')

        entries = []
        for e in Database.objects():
            e.now = e.now.encode('utf-8')

            check = e.now[5:7]
            check = int(check)


            # Look for matching Entries
            print "check %i, start %i" % (check,start)
            if check > start:
                line = str(e.num)+','+str(e.now)+','+str(e.sa)+','+str(e.message)+','+str(e.concern)
                f.write(line)
                f.write(cr)

        f.close()
        return render_template('managers/download.html', entries=entries)

    return render_template('managers/dateselect.html')


@managers_app.route('/name', methods=('GET', 'POST'))
def name():
    '''
    List all entries from the database by SA

    '''

    if request.method == 'POST':
        # Get desired project
        sa = request.form['sa']
        entries = []
        for e in Database.objects():
            if e.sa == sa:
                entries.append(e)
        return render_template('managers/listsaentryx.html', entries=entries, sa=sa)
    # Get engineers
    eng_list = []
    for eng in Engineers.objects():
        eng.name = eng.name.encode('utf-8')
        eng_list.append(eng.name)


    return render_template('managers/salistselect.html', eng_list=eng_list)
