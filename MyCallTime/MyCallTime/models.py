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

class Talent(db.Model):
    __tablename__ = 'Talent'
    ID = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.Time(7))
    name = db.Column(db.String(100))
    agency = db.Column(db.String(100))
    notes = db.Column(db.String(1000))
    shoot_id = db.Column(db.Integer, db.ForeignKey('Shoots.ID'))
    shoot = db.relationship(Shoots, backref='talent')

    # = db.relationship('Shoots', backref='Shoots')
    #theShoot = db.relationship(Shoots, backref='talent')

    def __init__(self, name=None, agency=None, notes=None, startTime=None):
        self.start_time = startTime
        self.name = name
        self.agency = agency
        self.notes = notes



class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    companycode = db.Column(db.String(100))

    def __init__(self, firstname, lastname, email, password, companycode):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.set_password(password)
        self.companycode = companycode
     
    def set_password(self, password):
        self.password = generate_password_hash(password)
   
    def check_password(self, password):
        return check_password_hash(self.password, password)