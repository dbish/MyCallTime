"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, flash, session, url_for, redirect, jsonify, json
from MyCallTime import app
from MyCallTime.forms import ContactForm, SignupForm, SignInForm, ShootsForm, EmailForm
from MyCallTime.models  import db
from MyCallTime.models import Shoots, User, Talent, Photo, Catering, Art, Makeup, Hair, Wardrobe, Production
from MyCallTime.models import ArtAssistants, ProdAssistants, PhotoAssistants, HairAssistants, MakeupAssistants, WardrobeAssistants
from wtforms.ext.sqlalchemy.orm import model_form
from flask_wtf import Form
from copy import deepcopy
from fpdf import FPDF, HTMLMixin
from flask.ext.mail import Message, Mail
import MyCallTime.config as config
Title = " "

mail = Mail(app)

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
    newShoot.copy(shoot)

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



from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet 
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from io import BytesIO
#from flask import Response
from flask import make_response

def myFirstPage(canvas, doc):

    PAGE_HEIGHT=defaultPageSize[1]
    PAGE_WIDTH=defaultPageSize[0]
    canvas.saveState()
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    canvas.restoreState()


def createPdf(title, date, location, id, shoot):
    #buffer = StringIO()
    buffer = BytesIO()
    styleSheet = getSampleStyleSheet()

    styleSheet = getSampleStyleSheet()
    PAGE_HEIGHT=defaultPageSize[1]
    PAGE_WIDTH=defaultPageSize[0]

    
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    # container for the 'Flowable' objects
    elements = []
    
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
    

    talentTable = Table(talentData)
    t=Table(data)
    
    elements.append(talentTable)
    elements.append(t)
    # write the document to buffer
    
    doc.build(elements, onFirstPage=myFirstPage)   
    pdf = buffer.getvalue()
    buffer.close()
    return pdf

@app.route('/viewpdf/<int:shoot_id>', methods=['GET'])
def createPDF(shoot_id):
    if 'email' not in session:
        return redirect(url_for('signin'))

    shoot = db.session.query(Shoots).get(shoot_id)
    pdf = createPdf(shoot.name, shoot.date, shoot.location, shoot.ID, shoot)
    response = make_response(pdf)


    response.headers['Content-Type']='application/pdf'
    response.headers['Content-Disposition'] = 'filename="shoot.pdf"'
    return response

@app.route('/savepdf/<int:shoot_id>', methods=['GET'])
def savePDF(shoot_id):
    if 'email' not in session:
        return redirect(url_for('signin'))

    shoot = db.session.query(Shoots).get(shoot_id)
    pdf = createPdf(shoot.name, shoot.date, shoot.location, shoot.ID, shoot)
    response = make_response(pdf)
    response.headers['Content-Type']='application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename="shoot.pdf"'

    return response

@app.route('/emailpdf/<int:shoot_id>', methods=['GET', 'POST'])
def emailPDF(shoot_id):
    if 'email' not in session:
        return redirect(url_for('signin'))

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
            return 'Email sent.'
      

    elif request.method == 'GET':
        form.cc.data=session['email']
        form.subject.data=shoot.name+" Call Sheet"
        form.message.data = "Attached is the call sheet for our upcoming shoot."
        return render_template('sendemail.html', form=form, id=shoot_id)