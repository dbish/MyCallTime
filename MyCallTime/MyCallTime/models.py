from flask_sqlalchemy import SQLAlchemy

from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

#class People(db.Model):
#    __tablename__ = 'People'
#    ID = db.Column(db.Integer, primary_key = True , autoincrement=False)
#    Name = db.Column(db.String(50))
#    Category= db.Column(db.String(15))
#    Phone = db.Column(db.Integer)
#    Email = db.Column(db.Integer)
#    Company = db.Column(db.Integer)

#    def __init__(self, id, name, category):
#        self.ID = id
#        self.Name = name
#        self.Category = category
#        self.Phone = 1
#        self.Email = 1
#        self.Company = 1

class Talent(db.Model):
    __tablename__ = 'Talent'
    ID = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.Time(7))
    name = db.Column(db.String(100))
    agency = db.Column(db.String(100))
    notes = db.Column(db.String(1000))
    shoot_id = db.Column(db.Integer, db.ForeignKey('Shoots.ID'))


    def __init__(self, name=None, agency=None, notes=None, startTime=None):
        self.start_time = startTime
        self.name = name
        self.agency = agency
        self.notes = notes

class Photo(db.Model):
    __tablename__= 'Photo'
    ID = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.Time(7))
    photographer = db.Column(db.String(100))
    digital_tech = db.Column(db.String(100))
    assistant = db.Column(db.String(100))
    notes = db.Column(db.String(1000))
    shoot_id = db.Column(db.Integer, db.ForeignKey('Shoots.ID'))

    def __init__(self, photo=None, digitech=None, ast=None, startTime=None, notes=None):
        self.start_time = startTime
        self.photographer = photo
        self.digital_tech = digitech
        self.assistant = ast
        self.notes = notes

class Art(db.Model):
    __tablename__= 'Art'
    ID = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.Time(7))
    artist = db.Column(db.String(100))
    assistant = db.Column(db.String(100))
    notes = db.Column(db.String(1000))
    shoot_id = db.Column(db.Integer, db.ForeignKey('Shoots.ID'))

    def __init__(self, artist=None, ast=None, startTime=None, notes=None):
        self.start_time = startTime
        self.artist = artist
        self.assistant = ast
        self.notes = notes

class Catering(db.Model):
    __tablename__= 'Catering'
    ID = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.Time(7))
    company = db.Column(db.String(100))
    contact = db.Column(db.String(100))
    notes = db.Column(db.String(1000))
    shoot_id = db.Column(db.Integer, db.ForeignKey('Shoots.ID'))

    def __init__(self, comp=None, cont=None, startTime=None, notes=None):
        self.start_time = startTime
        self.company = comp
        self.contact = cont
        self.notes = notes

class Makeup(db.Model):
    __tablename__= 'Makeup'
    ID = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.Time(7))
    artist = db.Column(db.String(100))
    assistant = db.Column(db.String(100))
    notes = db.Column(db.String(1000))
    shoot_id = db.Column(db.Integer, db.ForeignKey('Shoots.ID'))

    def __init__(self, artist=None, ast=None, startTime=None, notes=None):
        self.start_time = startTime
        self.artist = artist
        self.assistant = ast
        self.notes = notes

class Hair(db.Model):
    __tablename__= 'Hair'
    ID = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.Time(7))
    stylist = db.Column(db.String(100))
    assistant = db.Column(db.String(100))
    notes = db.Column(db.String(1000))
    shoot_id = db.Column(db.Integer, db.ForeignKey('Shoots.ID'))

    def __init__(self, stylist=None, ast=None, startTime=None, notes=None):
        self.start_time = startTime
        self.stylist = stylist
        self.assistant = ast
        self.notes = notes

class Wardrobe(db.Model):
    __tablename__= 'Wardrobe'
    ID = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.Time(7))
    stylist = db.Column(db.String(100))
    assistant = db.Column(db.String(100))
    notes = db.Column(db.String(1000))
    shoot_id = db.Column(db.Integer, db.ForeignKey('Shoots.ID'))

    def __init__(self, stylist=None, ast=None, startTime=None, notes=None):
        self.start_time = startTime
        self.stylist = stylist
        self.assistant = ast
        self.notes = notes

class Shoots(db.Model):
     __tablename__ = 'Shoots'
     ID = db.Column(db.Integer, primary_key = True)
     name = db.Column(db.String(100))
     client = db.Column(db.String(100))
     contact_name = db.Column(db.String(100))
     contact_email = db.Column(db.String(100))
     contact_phone = db.Column(db.String(50))
     date = db.Column(db.Date)
     start_time = db.Column(db.Time(7))
     wrap_time = db.Column(db.Time(7))
     location = db.Column(db.String(200))
     studio = db.Column(db.String(100))
    
     created_by =  db.Column(db.Integer)
     talent = db.relationship(Talent, cascade="all,delete")
     photo = db.relationship(Photo, uselist=False, cascade="all,delete")
     catering = db.relationship(Catering, uselist=False, cascade="all,delete")
     art = db.relationship(Art, uselist=False, cascade="all,delete")
     makeup = db.relationship(Makeup, uselist=False, cascade="all,delete")
     hair = db.relationship(Hair, uselist=False, cascade="all,delete")
     wardrobe = db.relationship(Wardrobe, uselist=False, cascade="all,delete")

     def __init__(self, name, client=None, contactName=None, contactEmail=None, contactPhone=None, date=None, startTime=None, 
                  wrapTime=None, location=None, studio=None):
        self.name = name
        self.client = client
        self.contact_name = contactName
        self.contact_email = contactEmail
        self.contact_phone = contactPhone
        self.date = date
        self.start_time = startTime
        self.wrap_time = wrapTime
        self.location = location
        self.studio = studio
    
     def clearID(self):
         self.ID = None
         for talent in self.talent:
             talent.ID = None
         
         photo.ID = None
         catering.ID = None
         art.ID = None
         makeup.ID = None
         hair.ID = None
         wardrobe.ID = None






class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    #companycode = db.Column(db.String(100))

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.set_password(password)
        #self.companycode = companycode
     
    def set_password(self, password):
        self.password = generate_password_hash(password)
   
    def check_password(self, password):
        return check_password_hash(self.password, password)