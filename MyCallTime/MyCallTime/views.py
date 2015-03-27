"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, flash, session, url_for, redirect, jsonify, json
from MyCallTime import app
from MyCallTime.forms import ContactForm, SignupForm, SignInForm, ShootsForm, EmailForm, MyAccountForm
from MyCallTime.models  import db
from MyCallTime.models import Shoots, User, Talent, Photo, Catering, Art, Makeup, Hair, Wardrobe, Production
from MyCallTime.models import ArtAssistants, ProdAssistants, PhotoAssistants, HairAssistants, MakeupAssistants, WardrobeAssistants
from wtforms.ext.sqlalchemy.orm import model_form
from flask_wtf import Form
from copy import deepcopy
from fpdf import FPDF, HTMLMixin
from flask.ext.mail import Message, Mail
import MyCallTime.config as config
from datetime import datetime
from pytz import timezone
from sqlalchemy import desc
import os

ALLOWED_EXTENSIONS=set(['png', 'jpg', 'jpeg'])
Title = " "

mail = Mail(app)

@app.route('/info')
def info():
    form = SignInForm()
    signupform=SignupForm() 
    return render_template('info.html', form=form, signupform=signupform)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    if 'email' not in session:
        return redirect(url_for('info'))

    user = db.session.query(User).filter_by(email=session['email']).first()
    user_uid = user.id

    allShoots = db.session.query(Shoots).filter_by(created_by=user_uid).filter(Shoots.archived!=True).order_by(desc(Shoots.last_updated)).all()

    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        shoots=allShoots,
        today=datetime.now(timezone('EST')).strftime('%Y-%m-%d')
    )




@app.route('/delete/<int:shoot_id>', methods=['GET'])
def deleteShoot(shoot_id):
     if 'email' not in session:
        return redirect(url_for('info'))
     shoot = db.session.query(Shoots).get(shoot_id)
     shoot.archived=True
     db.session.commit()
     return redirect(url_for('home'))


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/shoots/<int:shoot_id>', methods=['GET', 'POST'])
def viewShoot(shoot_id):
    if 'email' not in session:
        return redirect(url_for('info'))

    shoot = db.session.query(Shoots).get(shoot_id)
    form = ShootsForm(obj=shoot)

    if form.validate_on_submit():
        form.populate_obj(shoot)
        for talent in shoot.talent:
            if talent.archived == 1:
                shoot.talent.remove(talent)
        for assistant in shoot.art.assistants:
            if assistant.archived == 1:
                shoot.art.assistants.remove(assistant)
        for assistant in shoot.production.assistants:
            if assistant.archived == 1:
                shoot.production.assistants.remove(assistant)
        for assistant in shoot.photo.assistants:
            if assistant.archived == 1:
                shoot.photo.assistants.remove(assistant)
        for assistant in shoot.makeup.assistants:
            if assistant.archived == 1:
                shoot.makeup.assistants.remove(assistant)
        for assistant in shoot.hair.assistants:
            if assistant.archived == 1:
                shoot.hair.assistants.remove(assistant)
        for assistant in shoot.wardrobe.assistants:
            if assistant.archived == 1:
                shoot.wardrobe.assistants.remove(assistant)
        nowUTC = datetime.now(timezone('EST'))

        shoot.last_updated = nowUTC

        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], str(shoot_id)))

        db.session.commit()

        if request.form['viewPDF']=="true":
            return redirect(url_for('createPDF', shoot_id=shoot_id))

        if request.form['emailPDF']=="true":
            return redirect(url_for('emailPDF', shoot_id=shoot_id))

        flash('call sheet saved', 'success')
        return redirect(url_for('viewShoot', shoot_id=shoot_id))

    time = datetime.now(timezone('EST')) 
    if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], str(shoot_id))):
        hasImage = True 
    else:
        hasImage = False

    return render_template('edit.html', form=form, id=shoot_id, title=shoot.name, image=hasImage, time=time)

@app.route('/copy/<int:shoot_id>', methods=['GET'])
def copyShoot(shoot_id):
    if 'email' not in session:
        return redirect(url_for('info'))

    shoot = db.session.query(Shoots).get(shoot_id)
    newShoot = Shoots("")
    newShoot.copy(shoot)

    db.session.add(newShoot)
    form = ShootsForm(obj=newShoot)
    return render_template('edit.html', form=form, title="New Shoot")


@app.route('/newShoot', methods=['GET', 'POST'])
def newShoot():
    if 'email' not in session:
        return redirect(url_for('info'))

    user = db.session.query(User).filter_by(email=session['email']).first()
    user_uid = user.id

    newShoot = Shoots("")
    newShoot.created_by = user_uid
    newShoot.talent = [Talent()]
    newShoot.photo = Photo()
    newShoot.photo.assistants = [PhotoAssistants()]
    newShoot.catering = Catering()
    newShoot.art = Art()
    newShoot.art.assistants = [ArtAssistants()]
    newShoot.makeup = Makeup()
    newShoot.makeup.assistants = [MakeupAssistants()]
    newShoot.hair = Hair()
    newShoot.hair.assistants = [HairAssistants()]
    newShoot.wardrobe = Wardrobe()
    newShoot.wardrobe.assistants = [WardrobeAssistants()]
    newShoot.production = Production()
    newShoot.production.assistants = [ProdAssistants()]
    

    db.session.add(newShoot)

    form = ShootsForm(obj=newShoot)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(newShoot)
            for talent in newShoot.talent:
                if talent.archived == 1:
                    talent.shoot_id = None

            nowUTC = datetime.now(timezone('EST'))
            newShoot.last_updated = nowUTC



            db.session.commit()
            db.session.flush()
            db.session.refresh(newShoot)
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = file.filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], str(newShoot.ID)))

            return redirect(url_for('viewShoot', shoot_id=newShoot.ID))
        else:
            flash('failed validation')
    return render_template('edit.html', form=form, title="New Shoot")


@app.route('/myaccount', methods=['GET', 'POST'])
def myAccount():
    if 'email' not in session:
        return redirect(url_for('info'))
    user = db.session.query(User).filter_by(email=session['email']).first()

    form = MyAccountForm()
    
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('myaccount.html', form=form)
        else:  
            user.firstname = form.firstname.data
            user.lastname = form.lastname.data
            user.email = form.email.data
            if len(form.newpassword.data) > 0:
                user.set_password(newpassword)
            db.session.commit() 

            session['email'] = user.email
            return redirect(url_for('home'))
      
   
    elif request.method == 'GET':
        form.firstname.data = user.firstname
        form.lastname.data = user.lastname
        form.email.data = user.email
        return render_template('myaccount.html', form=form)


    

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
    return redirect(url_for('info'))
     
  session.pop('email', None)
  return redirect(url_for('home'))



from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet 
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from io import BytesIO
from flask import make_response

def myFirstPage(canvas, doc):

    PAGE_HEIGHT=defaultPageSize[1]
    PAGE_WIDTH=defaultPageSize[0]
    canvas.saveState()
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    canvas.restoreState()


def createPdf(title, date, location, id, shoot):
    buffer = BytesIO()
    styleSheet = getSampleStyleSheet()

    styleSheet = getSampleStyleSheet()
    PAGE_HEIGHT=defaultPageSize[1]
    PAGE_WIDTH=defaultPageSize[0]

    
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    # container for the 'Flowable' objects
    elements = []
    metaData = [[Paragraph('<b>Shoot Name</b>', styleSheet["BodyText"]), Paragraph('<b>Client</b>', styleSheet["BodyText"]), Paragraph('<b>Date</b>', styleSheet["BodyText"])]]
    metaData.append([shoot.name, shoot.client, shoot.date])
    metaData.append(['', '', ''])
    metaData.append([Paragraph('<b>Location</b>', styleSheet["BodyText"])])
    metaData.append([shoot.location, shoot.studio])
    metaData.append(['', '', ''])
    metaData.append([Paragraph('<b>Contact</b>', styleSheet["BodyText"])])
    metaData.append([shoot.contact_name, shoot.contact_phone, shoot.contact_email])
    metaData.append(['', '', ''])
    metaData.append([Paragraph('<b>Notes:</b>', styleSheet["BodyText"]), shoot.notes])
    metaData.append(['', '', ''])
    talentData= [[Paragraph('<b>Talent</b>', styleSheet["BodyText"]), Paragraph('<b>Agent</b>', styleSheet["BodyText"]), Paragraph('<b>Contact</b>', styleSheet["BodyText"]), Paragraph('<b>CallTime</b>', styleSheet["BodyText"])]]
    for talent in shoot.talent:
        talentData.append([talent.full_name, talent.agent_name, talent.agent_phone, talent.start_time])
    talentData.append(['', '', '', ''])
 
    data= [[Paragraph('<b>Team</b>', styleSheet["BodyText"]), Paragraph('<b>Name</b>', styleSheet["BodyText"]), Paragraph('<b>Contact</b>', styleSheet["BodyText"]), Paragraph('<b>CallTime</b>', styleSheet["BodyText"])]]
    
    #-production-
    #production company
    data.append(['Production Company', shoot.production.company, "", ""])
    #producer
    data.append(['Producer', shoot.production.producer_name, shoot.production.producer_phone, shoot.production.start_time])
    #production assist(s)
    for assistant in shoot.production.assistants:
        data.append(['Production Assist', assistant.assistantName, assistant.phone, shoot.production.start_time])


    
    #-photography-
    #photographer photographer contact-agent start_time
    data.append(['Photographer', shoot.photo.photographer, "contact agent", shoot.photo.start_time])
    #photo-agent agent_name agent_phone as-needed
    data.append(['Photo Agent', shoot.photo.agent_name,  shoot.photo.agent_phone, "as needed"])
    #digital tech
    data.append(['Digital Tech', shoot.photo.digital_tech, shoot.photo.digitech_phone, shoot.photo.start_time])
    #photo 1st assist
    data.append(['Photo 1st Assist', shoot.photo.first_ast_name, shoot.photo.first_ast_phone, shoot.photo.start_time])
    #photo assist(s)
    for assistant in shoot.photo.assistants:
        data.append(['Photo Assist', assistant.assistantName, assistant.phone, shoot.photo.start_time])

    #-art-
    data.append(['Artist', shoot.art.artist, "contact agent", shoot.art.start_time])
    data.append(['Art Agent', shoot.art.agent_name,  shoot.art.agent_phone, "as needed"])
    data.append(['Art 1st Assist', shoot.art.first_ast_name, shoot.art.first_ast_phone, shoot.art.start_time])
    for assistant in shoot.art.assistants:
        data.append(['Art Assist', assistant.assistantName, assistant.phone, shoot.art.start_time])

    #-makeup-
    data.append(['Makeup Artist', shoot.makeup.artist, "contact agent", shoot.makeup.start_time])
    data.append(['Makeup Agent', shoot.makeup.agent_name,  shoot.makeup.agent_phone, "as needed"])
    data.append(['Makeup 1st Assist', shoot.makeup.first_ast_name, shoot.makeup.first_ast_phone, shoot.makeup.start_time])
    for assistant in shoot.makeup.assistants:
        data.append(['Makeup Assist', assistant.assistantName, assistant.phone, shoot.makeup.start_time])

    #-hair-
    data.append(['Hair Stylist', shoot.hair.stylist, "contact agent", shoot.hair.start_time])
    data.append(['Hair Agent', shoot.hair.agent_name,  shoot.hair.agent_phone, "as needed"])
    data.append(['Hair 1st Assist', shoot.hair.first_ast_name, shoot.hair.first_ast_phone, shoot.hair.start_time])
    for assistant in shoot.hair.assistants:
        data.append(['Hair Assist', assistant.assistantName, assistant.phone, shoot.hair.start_time])

    #-wardrobe-
    data.append(['Wardrobe Stylist', shoot.wardrobe.stylist, "contact agent", shoot.wardrobe.start_time])
    data.append(['Wardrobe Agent', shoot.wardrobe.agent_name,  shoot.wardrobe.agent_phone, "as needed"])
    data.append(['Wardrobe 1st Assist', shoot.wardrobe.first_ast_name, shoot.wardrobe.first_ast_phone, shoot.wardrobe.start_time])
    for assistant in shoot.wardrobe.assistants:
        data.append(['Wardrobe Assist', assistant.assistantName, assistant.phone, shoot.wardrobe.start_time])


    #don't print rows where there is no name for a task
    data = [row for row in data if row[1] != '']
    
    cateringData = [[Paragraph('<b>Catering</b>', styleSheet["BodyText"])]]
    cateringData.append([shoot.catering.company_name, shoot.catering.company_phone, shoot.catering.company_email])
    cateringData.append([Paragraph('<i><b>breakfast:</b></i>', styleSheet["BodyText"]), shoot.catering.breakfast])
    cateringData.append([Paragraph('<i><b>lunch:</b></i>', styleSheet["BodyText"]), shoot.catering.lunch])
    cateringData.append([Paragraph('<i><b>notes:</b></i>', styleSheet["BodyText"]), shoot.catering.notes])

    talentTable = Table(talentData)
    t=Table(data)

    if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], str(id))):
        elements.append(Image(os.path.join(app.config['UPLOAD_FOLDER'], str(id)), height=140, width=190))

    elements.append(Table(metaData))
    elements.append(talentTable)
    elements.append(t)
    elements.append(Table(cateringData))

   

    # write the document to buffer
    
    doc.build(elements, onFirstPage=myFirstPage)   
    pdf = buffer.getvalue()
    buffer.close()
    return pdf

@app.route('/viewpdf/<int:shoot_id>', methods=['GET'])
def createPDF(shoot_id):
    if 'email' not in session:
        return redirect(url_for('info'))

    shoot = db.session.query(Shoots).get(shoot_id)
    pdf = createPdf(shoot.name, shoot.date, shoot.location, shoot.ID, shoot)
    response = make_response(pdf)


    response.headers['Content-Type']='application/pdf'
    response.headers['Content-Disposition'] = 'filename="shoot.pdf"'
    return response


@app.route('/savepdf/<int:shoot_id>', methods=['GET'])
def savePDF(shoot_id):
    if 'email' not in session:
        return redirect(url_for('info'))

    shoot = db.session.query(Shoots).get(shoot_id)
    pdf = createPdf(shoot.name, shoot.date, shoot.location, shoot.ID, shoot)
    response = make_response(pdf)
    response.headers['Content-Type']='application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename="shoot.pdf"'

    return response

@app.route('/emailpdf/<int:shoot_id>', methods=['GET', 'POST'])
def emailPDF(shoot_id):
    if 'email' not in session:
        return redirect(url_for('info'))

    form = EmailForm()
    shoot = db.session.query(Shoots).get(shoot_id)
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('sendemail.html', form=form, id=shoot_id)
        else:
            msg = Message(form.subject.data, sender=config.emailUsername, 
                          recipients=[form.recipient.data], cc=[form.cc.data])
            msg.body=form.message.data
            pdf = createPdf(shoot.name, shoot.date, shoot.location, shoot.ID, shoot)
            msg.attach("mycallsheet.pdf", "application/pdf", pdf)
            mail.send(msg)
            shoot.status="updates sent"
            db.session.commit()

            flash('call sheet emailed', 'success')

            return redirect(url_for('home'))

      

    elif request.method == 'GET':
        form.cc.data=session['email']
        form.subject.data=shoot.name+" Call Sheet"
        form.message.data = "Attached is the call sheet for our upcoming shoot."
        return render_template('sendemail.html', form=form, id=shoot_id)