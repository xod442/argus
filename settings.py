import os
SECRET_KEY = 'you-will-never-guess'
DEBUG=True
MONGODB_DB = 'sadbee'
HOSTNAME = 'https://127.0.0.1'
UPLOAD_FOLDER = '/app/static/images'
STATIC_IMAGE_URL = 'images'
#AWS_BUCKET = 'flaskbookrick'
#AWS_CONTENT_URL = 'https://s3-us-west-2.amazonaws.com'
AWS_SEND_MAIL = True
AWS_BUCKET = ''
AWS_CONTENT_URL = ''
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')
APP_TEMPLATE = os.path.join(APP_ROOT, 'templates')
