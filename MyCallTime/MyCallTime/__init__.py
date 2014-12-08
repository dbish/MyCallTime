"""
The flask application package.
"""

from flask import Flask
from MyCallTime.forms import ContactForm

app = Flask(__name__)

import MyCallTime.views
