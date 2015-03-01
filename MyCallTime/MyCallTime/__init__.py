"""
The flask application package.
"""

from flask import Flask
from MyCallTime.forms import ContactForm

from flask import g
from MyCallTime.models import db
import MyCallTime.config
from flask.ext.mail import Message, Mail
import os

mail = Mail()

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static\\uploads')



app = Flask(__name__)
app.secret_key = config.appKey
app.config['SQLALCHEMY_DATABASE_URI'] = config.connectionString
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = config.emailUsername
app.config["MAIL_PASSWORD"] = config.emailPassword
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
mail.init_app(app)
db.init_app(app) 
import MyCallTime.views


 


