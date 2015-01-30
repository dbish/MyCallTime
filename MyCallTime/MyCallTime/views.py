"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, flash, session, url_for, redirect, jsonify, json
from MyCallTime import app
from MyCallTime.forms import ContactForm, SignupForm, SignInForm, ShootsForm
from MyCallTime.models  import db
from MyCallTime.models import Shoots, User, Talent, Photo, Catering, Art, Makeup, Hair, Wardrobe
from wtforms.ext.sqlalchemy.orm import model_form
from flask_wtf import Form
from copy import deepcopy


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

@app.route('/delete/<int:shoot_id>', methods=['GET'])
def deleteShoot(shoot_id):
     if 'email' not in session:
        return redirect(url_for('signin'))
     shoot = db.session.query(Shoots).get(shoot_id)
     db.session.delete(shoot)
     db.session.commit()
     return redirect(url_for('home'))

@app.route('/shoots/<int:shoot_id>', methods=['GET', 'POST'])
def viewShoot(shoot_id):
    if 'email' not in session:
        return redirect(url_for('signin'))

    shoot = db.session.query(Shoots).get(shoot_id)
    form = ShootsForm(obj=shoot)

    if form.validate_on_submit():
        form.populate_obj(shoot)
        db.session.commit()
    
    return render_template('edit.html', form=form, id=shoot_id, title=shoot.name)

@app.route('/copy/<int:shoot_id>', methods=['GET'])
def copyShoot(shoot_id):
    if 'email' not in session:
        return redirect(url_for('signin'))

    shoot = db.session.query(Shoots).get(shoot_id)
    newShoot = Shoots("")
    newShoot.client = shoot.client
    newShoot.contact_name = shoot.contact_name
    newShoot.contact_email = shoot.contact_email
    newShoot.contact_phone = shoot.contact_phone
    newShoot.start_time = shoot.start_time
    newShoot.wrap_time = shoot.wrap_time
    newShoot.location = shoot.location
    newShoot.studio = shoot.studio
    newShoot.created_by = shoot.created_by
    newShoot.talent = [Talent()]
    newShoot.photo = Photo()
    newShoot.catering = Catering()
    newShoot.art = Art()
    newShoot.makeup = Makeup()
    newShoot.hair = Hair()
    newShoot.wardrobe = Wardrobe()


    db.session.add(newShoot)
    form = ShootsForm(obj=newShoot)
    return render_template('edit.html', form=form, title="New Shoot")


@app.route('/newShoot', methods=['GET', 'POST'])
def newShoot():
    if 'email' not in session:
        return redirect(url_for('signin'))

    user = db.session.query(User).filter_by(email=session['email']).first()
    user_uid = user.id

    newShoot = Shoots("")
    newShoot.created_by = user_uid
    newShoot.talent = [Talent()]
    newShoot.photo = Photo()
    newShoot.catering = Catering()
    newShoot.art = Art()
    newShoot.makeup = Makeup()
    newShoot.hair = Hair()
    newShoot.wardrobe = Wardrobe()

    db.session.add(newShoot)

    form = ShootsForm(obj=newShoot)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(newShoot)
            db.session.commit()
            db.session.flush()
            db.session.refresh(newShoot)
            return redirect(url_for('viewShoot', shoot_id=newShoot.ID))
        else:
            flash('failed validation')
    return render_template('edit.html', form=form, title="New Shoot")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:  
      newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
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

@app.route('/pdf/<int:shoot_id>', methods=['GET'])
def createPDF(shoot_id):
    if 'email' not in session:
        return redirect(url_for('signin'))

    shoot = db.session.query(Shoots).get(shoot_id)
    form = ShootsForm(obj=shoot)
    if form.validate_on_submit():
        form.populate_obj(shoot)
        db.session.commit()
    
    return ()