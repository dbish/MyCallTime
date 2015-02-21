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
#        self.assistantName = assistantName
#        self.Category = category
#        self.Phone = 1
#        self.Email = 1
#        self.Company = 1

class ProdAssistants(db.Model):
    __tablename__ = 'ProdAssistants'
    ID = db.Column(db.Integer, primary_key = True)
    assistantName = db.Column(db.String(50))
    email = db.Column(db.String(50), info={'placeholder': 'email'})
    phone = db.Column(db.String(50))
    prod_id = db.Column(db.Integer, db.ForeignKey('Production.ID'))

    def __init__(self, assistantName=None, email=None, phone=None):
        self.assistantName = assistantName
        self.email = email
        self.phone = phone
    
    def createCopy(self):
        return ProdAssistants(self.assistantName, self.email, self.phone)

class PhotoAssistants(db.Model):
    __tablename__ = 'PhotoAssistants'
    ID = db.Column(db.Integer, primary_key = True)
    assistantName = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    photo_id = db.Column(db.Integer, db.ForeignKey('Photo.ID'))

    def __init__(self, assistantName=None, email=None, phone=None):
        self.assistantName = assistantName
        self.email = email
        self.phone = phone
    
    def createCopy(self):
        return PhotoAssistants(self.assistantName, self.email, self.phone)

class WardrobeAssistants(db.Model):
    __tablename__ = 'WardrobeAssistants'
    ID = db.Column(db.Integer, primary_key = True)
    assistantName = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    wardrobe_id = db.Column(db.Integer, db.ForeignKey('Wardrobe.ID'))

    def __init__(self, assistantName=None, email=None, phone=None):
        self.assistantName = assistantName
        self.email = email
        self.phone = phone
    
    def createCopy(self):
        return WardrobeAssistants(self.assistantName, self.email, self.phone)

class HairAssistants(db.Model):
    __tablename__ = 'HairAssistants'
    ID = db.Column(db.Integer, primary_key = True)
    assistantName = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    hair_id = db.Column(db.Integer, db.ForeignKey('Hair.ID'))

    def __init__(self, assistantName=None, email=None, phone=None):
        self.assistantName = assistantName
        self.email = email
        self.phone = phone
    
    def createCopy(self):
        return HairAssistants(self.assistantName, self.email, self.phone)

class MakeupAssistants(db.Model):
    __tablename__ = 'MakeupAssistants'
    ID = db.Column(db.Integer, primary_key = True)
    assistantName = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    makeup_id = db.Column(db.Integer, db.ForeignKey('Makeup.ID'))

    def __init__(self, assistantName=None, email=None, phone=None):
        self.assistantName = assistantName
        self.email = email
        self.phone = phone
    
    def createCopy(self):
        return MakeupAssistants(self.assistantName, self.email, self.phone)

class ArtAssistants(db.Model):
    __tablename__ = 'ArtAssistants'
    ID = db.Column(db.Integer, primary_key = True)
    assistantName = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    art_id = db.Column(db.Integer, db.ForeignKey('Art.ID'))

    def __init__(self, assistantName=None, email=None, phone=None):
        self.assistantName = assistantName
        self.email = email
        self.phone = phone
    
    def createCopy(self):
        return ArtAssistants(self.assistantName, self.email, self.phone)

class Production(db.Model):
    __tablename__ = 'Production'
    ID = db.Column(db.Integer, primary_key = True)
    company = db.Column(db.String(50))
    start_time = db.Column(db.Time(7))
    producer_name = db.Column(db.String(50))
    producer_email = db.Column(db.String(50))
    producer_phone = db.Column(db.String(50))
    shoot_id = db.Column(db.Integer, db.ForeignKey('Shoots.ID'))
    assistants = db.relationship(ProdAssistants, cascade="all,delete")

    def __init__(self, company=None, time=None, name=None, email=None, phone=None):
        self.company = company
        self.start_time = time
        self.producer_name = name
        self.producer_email = email
        self.producer_phone = phone

    def createCopy(self):
        return Production(self.company, self.start_time, self.producer_name, self.producer_email, self.producer_phone)

class Talent(db.Model):
    __tablename__ = 'Talent'
    ID = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(100))
    start_time = db.Column(db.Time(7))
    agent_name = db.Column(db.String(50))
    agent_email = db.Column(db.String(50))
    agent_phone = db.Column(db.String(50))
    shoot_id = db.Column(db.Integer, db.ForeignKey('Shoots.ID'))
    archived = db.Column(db.SmallInteger)


    def __init__(self, name=None, agentName=None, startTime=None, email=None, phone=None):
        self.start_time = startTime
        self.full_name = name
        self.agent_name = agentName
        self.agent_email = email
        self.agent_phone = phone
    

    def createCopy(self):
        return Talent(self.full_name, self.agent_name, self.start_time, self.agent_email, self.agent_phone)

class Photo(db.Model):
    __tablename__= 'Photo'
    ID = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.Time(7))
    photographer = db.Column(db.String(100))
    agent_name = db.Column(db.String(50))
    agent_email = db.Column(db.String(50))
    agent_phone = db.Column(db.String(50))
    digital_tech = db.Column(db.String(100))
    digitech_email = db.Column(db.String(50))
    digitech_phone = db.Column(db.String(50))
    first_ast_name = db.Column(db.String(50))
    first_ast_email = db.Column(db.String(50))
    first_ast_phone = db.Column(db.String(50))
    shoot_id = db.Column(db.Integer, db.ForeignKey('Shoots.ID'))
    assistants = db.relationship(PhotoAssistants, cascade="all,delete")

    def __init__(self, photo=None, digitech=None, startTime=None, agent=None, agentEmail=None, agentPhone=None,
                 digiEmail=None, digiPhone=None, firstAst=None, firstAstEmail=None, firstAstPhone=None):
        self.start_time = startTime
        self.photographer = photo
        self.agent_name = agent
        self.agent_email = agentEmail
        self.agent_phone = agentPhone
        self.digital_tech = digitech
        self.digitech_email = digiEmail
        self.digitech_phone = digiPhone
        self.first_ast_name = firstAst
        self.first_ast_email = firstAstEmail
        self.first_ast_phone = firstAstPhone
        


    def createCopy(self):
        return Photo(self.photographer, self.digital_tech,  self.start_time, self.agent_name, self.agent_email, self.agent_phone,
                 self.digitech_email, self.digitech_phone, self.first_ast_name, self.first_ast_email, self.first_ast_phone)

class Art(db.Model):
    __tablename__= 'Art'
    ID = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.Time(7))
    artist = db.Column(db.String(100))
    agent_name = db.Column(db.String(50))
    agent_email = db.Column(db.String(50))
    agent_phone = db.Column(db.String(50))
    first_ast_name = db.Column(db.String(50))
    first_ast_email = db.Column(db.String(50))
    first_ast_phone = db.Column(db.String(50))
    assistants = db.relationship(ArtAssistants, cascade="all,delete")
    
    shoot_id = db.Column(db.Integer, db.ForeignKey('Shoots.ID'))

    def __init__(self, artist=None, startTime=None, agent=None, agentEmail=None, agentPhone=None,
                 firstAst=None, firstAstEmail=None, firstAstPhone=None):
        self.start_time = startTime
        self.artist = artist
        self.agent_name = agent
        self.agent_email = agentEmail
        self.agent_phone = agentPhone
        self.first_ast_name = firstAst
        self.first_ast_email = firstAstEmail
        self.first_ast_phone = firstAstPhone

    def createCopy(self):
        return Art(self.artist, self.start_time, self.agent_name, self.agent_email, self.agent_phone, 
                   self.first_ast_name, self.first_ast_email, self.first_ast_phone)


class Catering(db.Model):
    __tablename__= 'Catering'
    ID = db.Column(db.Integer, primary_key = True)
    breakfast = db.Column(db.Time(7))
    lunch = db.Column(db.Time(7))
    company_name = db.Column(db.String(100))
    company_email = db.Column(db.String(50))
    company_phone = db.Column(db.String(50))
    notes = db.Column(db.String(1000))
    shoot_id = db.Column(db.Integer, db.ForeignKey('Shoots.ID'))


    def __init__(self, comp=None, notes=None, compEmail=None, compPhone=None, breakfast=None, lunch=None):
        self.company_name = comp
        self.company_email = compEmail
        self.company_phone = compPhone
        self.breakfast = breakfast
        self.lunch = lunch
        self.notes = notes

    def createCopy(self):
        return Catering(self.company_name, self.notes, self.company_email, self.company_phone, self.breakfast, self.lunch)

class Makeup(db.Model):
    __tablename__= 'Makeup'
    ID = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.Time(7))
    artist = db.Column(db.String(100))
    agent_name = db.Column(db.String(50))
    agent_email = db.Column(db.String(50))
    agent_phone = db.Column(db.String(50))
    first_ast_name = db.Column(db.String(50))
    first_ast_email = db.Column(db.String(50))
    first_ast_phone = db.Column(db.String(50))
    assistants = db.relationship(MakeupAssistants, cascade="all,delete")
    
    shoot_id = db.Column(db.Integer, db.ForeignKey('Shoots.ID'))

    def __init__(self, artist=None, startTime=None, agent=None, agentEmail=None, agentPhone=None,
                 firstAst=None, firstAstEmail=None, firstAstPhone=None):
        self.start_time = startTime
        self.artist = artist
        self.agent_name = agent
        self.agent_email = agentEmail
        self.agent_phone = agentPhone
        self.first_ast_name = firstAst
        self.first_ast_email = firstAstEmail
        self.first_ast_phone = firstAstPhone

    def createCopy(self):
        return Makeup(self.artist, self.start_time, self.agent_name, self.agent_email, self.agent_phone, 
                   self.first_ast_name, self.first_ast_email, self.first_ast_phone)

class Hair(db.Model):
    __tablename__= 'Hair'
    ID = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.Time(7))
    stylist = db.Column(db.String(100))
    agent_name = db.Column(db.String(50))
    agent_email = db.Column(db.String(50))
    agent_phone = db.Column(db.String(50))
    first_ast_name = db.Column(db.String(50))
    first_ast_email = db.Column(db.String(50))
    first_ast_phone = db.Column(db.String(50))
    assistants = db.relationship(HairAssistants, cascade="all,delete")

    shoot_id = db.Column(db.Integer, db.ForeignKey('Shoots.ID'))

    def __init__(self, stylist=None, startTime=None, agent=None, agentEmail=None, agentPhone=None,
                 firstAst=None, firstAstEmail=None, firstAstPhone=None):
        self.start_time = startTime
        self.stylist = stylist
        self.agent_name = agent
        self.agent_email = agentEmail
        self.agent_phone = agentPhone
        self.first_ast_name = firstAst
        self.first_ast_email = firstAstEmail
        self.first_ast_phone = firstAstPhone

    def createCopy(self):
        return Hair(self.stylist, self.start_time, self.agent_name, self.agent_email, self.agent_phone, 
                   self.first_ast_name, self.first_ast_email, self.first_ast_phone)

class Wardrobe(db.Model):
    __tablename__= 'Wardrobe'
    ID = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.Time(7))
    stylist = db.Column(db.String(100))
    agent_name = db.Column(db.String(50))
    agent_email = db.Column(db.String(50))
    agent_phone = db.Column(db.String(50))
    first_ast_name = db.Column(db.String(50))
    first_ast_email = db.Column(db.String(50))
    first_ast_phone = db.Column(db.String(50))
    shoot_id = db.Column(db.Integer, db.ForeignKey('Shoots.ID'))
    assistants = db.relationship(WardrobeAssistants, cascade="all,delete")

    def __init__(self, stylist=None, startTime=None, agent=None, agentEmail=None, agentPhone=None,
                 firstAst=None, firstAstEmail=None, firstAstPhone=None):
        self.start_time = startTime
        self.stylist = stylist
        self.agent_name = agent
        self.agent_email = agentEmail
        self.agent_phone = agentPhone
        self.first_ast_name = firstAst
        self.first_ast_email = firstAstEmail
        self.first_ast_phone = firstAstPhone

    def createCopy(self):
        return Wardrobe(self.stylist, self.start_time, self.agent_name, self.agent_email, self.agent_phone, 
                   self.first_ast_name, self.first_ast_email, self.first_ast_phone)


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
     notes = db.Column(db.String(1000))
     
    
     created_by =  db.Column(db.Integer)
     archived = db.Column(db.Boolean)
     talent = db.relationship(Talent, cascade="all,delete")
     photo = db.relationship(Photo, uselist=False, cascade="all,delete")
     catering = db.relationship(Catering, uselist=False, cascade="all,delete")
     art = db.relationship(Art, uselist=False, cascade="all,delete")
     makeup = db.relationship(Makeup, uselist=False, cascade="all,delete")
     hair = db.relationship(Hair, uselist=False, cascade="all,delete")
     wardrobe = db.relationship(Wardrobe, uselist=False, cascade="all,delete")
     production = db.relationship(Production, uselist=False, cascade="all,delete")

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
    
     def copy(self, toCopy):
        self.name = toCopy.name
        self.client = toCopy.client
        self.contact_name = toCopy.contact_name
        self.contact_email = toCopy.contact_email
        self.contact_phone = toCopy.contact_phone
        self.start_time = toCopy.start_time
        self.wrap_time = toCopy.wrap_time
        self.location = toCopy.location
        self.studio = toCopy.studio
        self.talent = []
        for talent in toCopy.talent:
             self.talent.append(talent.createCopy())
         
        self.photo = toCopy.photo.createCopy()
        self.catering = toCopy.catering.createCopy()
        self.art = toCopy.art.createCopy()
        self.makeup = toCopy.makeup.createCopy()
        self.hair = toCopy.hair.createCopy()
        self.wardrobe = toCopy.wardrobe.createCopy()
        self.production = toCopy.production.createCopy()
  

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