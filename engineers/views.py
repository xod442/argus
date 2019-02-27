
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

Flask script that manages tasks and concernse for field SAs
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

engineers_app = Blueprint('engineers_app', __name__)

@engineers_app.route('/newentry', methods=('GET', 'POST'))
def newentry():
    '''
    Adds a new entry to the database
    Reads form variables, creates an entry and
    saves it to the mongo database..

    '''
    # Get sa
    sa_list= []
    for sa in Temp.objects():
        sa_list.append(sa.sa)
    sa = sa_list[0]
    sa = sa.encode('utf-8')
    sa=sa.replace(" ", "-")

    # Get time date stamp
    now = datetime.datetime.now()
    now = now.isoformat()


    # Get next record number and add 1
    num_list= []
    for n in Number.objects():
        num_list.append(n.num)
    num = num_list[0]
    more = [sa,now,num]

    # rick.append('fail')
    error='none'
    form = DatabaseForm()
    if form.validate_on_submit():
        message=form.message.data
        concern=form.concern.data

        message = message.encode('utf-8')
        concern = concern.encode('utf-8')

        # Build record to write to mongo database

        entry = Database(sa=sa,message=message,concern=concern,now=now,num=num)
        #rick.append('faiul')

        # Save the record
        try:
            entry.save()
        except:
            return render_template('engineers/dberror2.html',error=error)

        # Increment number for next use
        num = num + 1

        # Clear temp database for a new session
        Number.objects().delete()

        # write the new number
        update = Number(num=num)

        # Save the number record for the next use
        try:
            update.save()
        except:
            return render_template('engineers/dberror3.html')


        return render_template('engineers/savedentry.html')
    return render_template('engineers/newentry.html', form=form, more=more)

@engineers_app.route('/editentry', methods=('GET', 'POST'))
def editentry():
    '''
    Edit an existing entry from the database

    '''
    if request.method == 'POST':
        # Get desired project
        num = request.form['num']
        # PDelete the record from mongo database
        entry = Database.objects(num=num)

        # create list from database entry
        more = {
                "num" : entry[0].num,
                "now" : entry[0].now,
                "sa" : entry[0].sa,
                "message" : entry[0].message,
                "concern" : entry[0].concern
                }
        # rick.append('fail')
        #send form with info list
        return render_template('engineers/editentry.html', more=more)
    # Get sa
    sa_list= []
    for sa in Temp.objects():
        sa_list.append(sa.sa)
    sa = sa_list[0]
    sa = sa.encode('utf-8')
    sa=sa.replace(" ", "-")

    entries = []
    for e in Database.objects():
        if e.sa == sa:
            entries.append(e.num)
    return render_template('engineers/entryeditselect.html', entries=entries)

@engineers_app.route('/upentry', methods=('GET', 'POST'))
def upentry():
    '''
    Saves the edited record

    '''
    # Get desired project
    num = request.form['num']
    now = request.form['now']
    sa = request.form['sa']
    message = request.form['message']
    concern = request.form['concern']

    now = now.encode('utf-8')
    sa = sa.encode('utf-8')
    message = message.encode('utf-8')
    concern = concern.encode('utf-8')
    num = int(num)

    # Save the number record for the next use

    try:
        Database.objects(num=num).update(message=message,concern=concern)
    except:
        return render_template('engineers/dberror2.html')

    #send delete success
    return render_template('engineers/goodeditentry.html')



@engineers_app.route('/deleteentry', methods=('GET', 'POST'))
def deleteentry():
    '''
    Delete an existing entry from the database

    '''
    if request.method == 'POST':
        # Get desired project
        num = request.form['num']
        # PDelete the record from mongo database
        try:
            Database.objects(num=num).delete()
        except:

            return render_template('engineers/dberror4.html')

        #send delete success
        return render_template('engineers/deleteentry.html')

    # Build list of projects in database and send to selector form

    # Get sa
    sa_list= []
    for sa in Temp.objects():
        sa_list.append(sa.sa)
    sa = sa_list[0]
    sa = sa.encode('utf-8')
    sa=sa.replace(" ", "-")

    entries = []
    for e in Database.objects():
        if e.sa == sa:
            entries.append(e.num)
    return render_template('engineers/entryeditdelete.html', entries=entries)

@engineers_app.route('/listentry', methods=('GET', 'POST'))
def listentry():
    '''
    List all entries from the database by SA

    '''
    # Get sa
    sa_list= []
    for sa in Temp.objects():
        sa_list.append(sa.sa)
    sa = sa_list[0]
    sa = sa.encode('utf-8')
    sa=sa.replace(" ", "-")

    entries = []
    for e in Database.objects():
        if e.sa == sa:
            entries.append(e)
    return render_template('engineers/listentry.html', entries=entries)


@engineers_app.route('/cloneentry', methods=('GET', 'POST'))
def cloneentry():
    '''
    Clone an existing entry from the database

    '''
    if request.method == 'POST':
        # Get desired project
        num = request.form['num']
        # PDelete the record from mongo database
        entry = Database.objects(num=num)

        # Get next record number and add 1
        num_list= []
        for n in Number.objects():
            num_list.append(n.num)
        num = num_list[0]

        # Get time date stamp
        now = datetime.datetime.now()
        now = now.isoformat()


        # create list from database entry
        more = {
                "num" : num,
                "now" : now,
                "sa" : entry[0].sa,
                "message" : entry[0].message,
                "concern" : entry[0].concern
                }


        #send form with info list
        return render_template('engineers/cloneentry.html', more=more)
    # Get sa
    sa_list= []
    for sa in Temp.objects():
        sa_list.append(sa.sa)
    sa = sa_list[0]
    sa = sa.encode('utf-8')
    sa=sa.replace(" ", "-")

    entries = []
    for e in Database.objects():
        if e.sa == sa:
            entries.append(e.num)
    return render_template('engineers/entrycloneselect.html', entries=entries)


@engineers_app.route('/upclone', methods=('GET', 'POST'))
def upclone():
    '''
    Saves the cloned record

    '''
    # Get desired project
    num = request.form['num']
    now = request.form['now']
    sa = request.form['sa']
    message = request.form['message']
    concern = request.form['concern']

    now = now.encode('utf-8')
    sa = sa.encode('utf-8')
    message = message.encode('utf-8')
    concern = concern.encode('utf-8')
    num = int(num)

    # Build record to write to mongo database

    entry = Database(sa=sa,message=message,concern=concern,now=now,num=num)
    #rick.append('faiul')

    # Save the record
    try:
        entry.save()
    except:
        error = "Clone save issues"
        return render_template('engineers/dberror2.html',error=error)

    # Increment number for next use
    num = num + 1

    # Clear temp database for a new session
    Number.objects().delete()

    # write the new number
    update = Number(num=num)

    # Save the number record for the next use
    try:
        update.save()
    except:
        return render_template('engineers/dberror3.html')
    return render_template('engineers/goodeditentry.html')
