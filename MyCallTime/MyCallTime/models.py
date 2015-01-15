from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

class People(db.Model):
    __tablename__ = 'People'
    ID = db.Column(db.Integer, primary_key = True , autoincrement=False)
    Name = db.Column(db.String(50))
    Category= db.Column(db.String(15))
    Phone = db.Column(db.Integer)
    Email = db.Column(db.Integer)
    Company = db.Column(db.Integer)

    def __init__(self, id, name, category):
        self.ID = id
        self.Name = name
        self.Category = category
        self.Phone = 1
        self.Email = 1
        self.Company = 1

class Shoots(db.Model):
     __tablename__ = 'Shoots'
     ID = db.Column(db.Integer, primary_key = True , autoincrement=False)
     UserName = db.Column(db.String(50))
     Name = db.Column(db.String(15))
     Date = db.Column(db.Date)
     StartTime = db.Column(db.Time(7))
     EndTime = db.Column(db.Time(7))
     Client = db.Column(db.String(50))
     Location = db.Column(db.String(50))
     Studio = db.Column(db.String(50))

     def __init__(self, id, name):
        self.ID = id
        self.UserName = "user"+name
        self.Name = name
        self.Date = None
        self.StartTime = None
        self.EndTime = None
        self.Client = None
        self.Location = None
        self.Studio = None

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