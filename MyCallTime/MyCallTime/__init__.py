"""
The flask application package.
"""

from flask import Flask
from MyCallTime.forms import ContactForm

from flask import g
import pypyodbc as pyodbc


app = Flask(__name__)



import MyCallTime.views
