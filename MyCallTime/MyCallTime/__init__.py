"""
The flask application package.
"""

from flask import Flask
from MyCallTime.forms import ContactForm

from flask import g
from MyCallTime.models import db
import MyCallTime.config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.connectionString

db.init_app(app) 
import MyCallTime.views


 


