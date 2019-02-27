

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
from flask import Blueprint, render_template, request, redirect, session, url_for, abort
import os
from werkzeug import secure_filename
from mongoengine import Q

# Place to stach the user temporarily
from database.temp import Temp

main_app = Blueprint('main_app', __name__)

@main_app.route('/main', methods=('GET', 'POST'))
@main_app.route('/', methods=('GET', 'POST'))
@main_app.route('/index', methods=('GET', 'POST'))
def main():
    ''' Delete any residual links in the db and display the main menu
    '''
    # Clear temp database for a new session
    Temp.objects().delete()

    return render_template('main/main.html')

@main_app.route('/help', methods=('GET', 'POST'))
def help():

    return render_template('main/help.html')

@main_app.route('/main_select', methods=('GET', 'POST'))
def main_select():
    sa = request.form['sa']
    # Stash the user
    # Build record to write to mongo database

    temp = Temp(sa=sa)
    # Save the record
    try:
        temp.save()
    except:
        return render_template('engineers/dberror.html')

    if sa == 'Rick Hawkins':
        return render_template('main/manager.html', sa=sa)
    else:
        return render_template('main/engineer.html', sa=sa)

@main_app.route('/main_engineer', methods=('GET', 'POST'))
def main_engineer():

    # Get sa
    sa_list= []
    for sa in Temp.objects():
        sa_list.append(sa.sa)
    sa = sa_list[0]
    sa = sa.encode('utf-8')
    sa=sa.replace(" ", "-")


    return render_template('main/engineer.html', sa=sa)

@main_app.route('/main_manager', methods=('GET', 'POST'))
def main_manager():

    # Get sa
    sa_list= []
    for sa in Temp.objects():
        sa_list.append(sa.sa)
    sa = sa_list[0]
    sa = sa.encode('utf-8')
    sa=sa.replace(" ", "-")


    return render_template('main/manager.html', sa=sa)
