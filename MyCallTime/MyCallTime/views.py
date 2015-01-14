"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from MyCallTime import app
from MyCallTime.forms import ContactForm
from MyCallTime.models  import db
from MyCallTime.models import People, Shoots


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
  
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year
        
    )

@app.route('/contact') 
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/newSheet')
def newSheet():
    """Renders the about page."""
   
    newEntry = Shoots(123, "shoot 2")
    db.session.add(newEntry)
    db.session.commit()

    return render_template(
        'newSheet.html',
        title='test',
        year=datetime.now().year,
        message='Your application description page.',
       
    )
