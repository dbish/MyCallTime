"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, flash, session, url_for, redirect, jsonify, json
from MyCallTime import app
from MyCallTime.forms import ContactForm, SignupForm, SignInForm, ShootsForm
from MyCallTime.models  import db
from MyCallTime.models import Shoots, User, Talent
from wtforms.ext.sqlalchemy.orm import model_form
from flask_wtf import Form


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    if 'email' not in session:
        return redirect(url_for('signin'))

    user = db.session.query(User).filter_by(email=session['email']).first()
    user_uid = user.id

    allShoots = db.session.query(Shoots).filter_by(created_by=user_uid).all()

    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        shoots=allShoots
    )

#@app.route('/contact') 
#def contact():
#    """Renders the contact page."""
#    return render_template(
#        'contact.html',
#        title='Contact',
#        year=datetime.now().year,
#        message='Your contact page.'
#    )

#@app.route('/about')
#def about():
#    """Renders the about page."""
#    return render_template(
#        'about.html',
#        title='About',
#        year=datetime.now().year,
#        message='Your application description page.'
#    )

#@app.route('/save', methods = ['POST'])
#def save():
#    results = request.form
#    #results = request.get_json()

#    return jsonify(result=str(results))
    

#@app.route('/newSheet')
#def newSheet():
#    """Renders the about page."""
   
#    #newShoot = Shoots("diamond's shoot")
#    #newShoot.talent = [Talent(name="diamond")]
#    #db.session.add(newShoot)
#    #db.session.commit()

#    newShoot = Shoots("")

#    return render_template(
#        'newSheet.html',
#        shoot=newShoot,
#        year=datetime.now().year,
#        message='Your application description page.',
       
#    )

@app.route('/shoots/<int:shoot_id>', methods=['GET', 'POST'])
def viewShoot(shoot_id):
    if 'email' not in session:
        return redirect(url_for('signin'))

    shoot = db.session.query(Shoots).get(shoot_id)
   
    form = ShootsForm(obj=shoot)
    if form.validate_on_submit():
        form.populate_obj(shoot)
        db.session.commit()
    
    return render_template('edit.html', form=form, id=shoot_id)


@app.route('/newShoot', methods=['GET', 'POST'])
def newShoot():
    if 'email' not in session:
        return redirect(url_for('signin'))

    user = db.session.query(User).filter_by(email=session['email']).first()
    user_uid = user.id

    newShoot = Shoots("")
    newShoot.created_by = user_uid
    db.session.add(newShoot)
    form = ShootsForm(obj=newShoot)
    if form.validate_on_submit():
        form.populate_obj(newShoot)
        db.session.commit()
        db.session.flush()
        db.session.refresh(newShoot)
        return redirect(url_for('viewShoot', shoot_id=newShoot.ID))
    return render_template('edit.html', form=form)


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


@app.route('/signin', methods=['GET', 'POST'])
def signin():
  form = SignInForm()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signin.html', form=form)
    else:
      session['email'] = form.email.data
      return redirect(url_for('home'))
                 
  elif request.method == 'GET':
    return render_template('signin.html', form=form)

@app.route('/signout')
def signout():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
     
  session.pop('email', None)
  return redirect(url_for('home'))