
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

#from project.models import Project
#from project.forms import ProjectForm

managers_app = Blueprint('managers_app', __name__)

@managers_app.route('/listentrys', methods=('GET', 'POST'))
def listentrys():
    '''
    Adds a new project to the project database
    Reads form variables, creates a project variable and
    saves it to the mongo database.

    '''

    return render_template('main/main.html')
