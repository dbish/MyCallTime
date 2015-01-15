"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, flash, session, url_for, redirect
from MyCallTime import app
from MyCallTime.forms import ContactForm, SignupForm
from MyCallTime.models  import db
from MyCallTime.models import People, Shoots, User


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    if 'email' not in session:
        return redirect(url_for('signin'))

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
   
    #newEntry = Shoots(123, "shoot 2")
    #db.session.add(newEntry)
    #db.session.commit()

    return render_template(
        'newSheet.html',
        title='test',
        year=datetime.now().year,
        message='Your application description page.',
       
    )

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:  
      newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data, form.companycode.data)
      db.session.add(newuser)
      db.session.commit() 

      session['email'] = newuser.email
      return redirect(url_for('home'))
      
   
  elif request.method == 'GET':
    return render_template('signup.html', form=form)