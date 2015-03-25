from flask_wtf import Form
from wtforms import StringField, TextAreaField, TextField, SubmitField, ValidationError, validators, PasswordField
from MyCallTime.models import db, User, Shoots, Talent, Photo, Catering, Art, Makeup, Hair, Wardrobe, Production
from MyCallTime.models import ArtAssistants, ProdAssistants, PhotoAssistants, HairAssistants, MakeupAssistants, WardrobeAssistants
from wtforms_alchemy import ModelForm, model_form_factory, ModelFieldList, ModelFormField
from wtforms.fields import FormField
from sqlalchemy import func
from flask import session

BaseModelForm = model_form_factory(Form)



class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

class TalentForm(ModelForm):
    class Meta:
        model = Talent
        
    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(TalentForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

class ArtAssistantsForm(ModelForm):
    class Meta:
        model = ArtAssistants

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(ArtAssistantsForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

class ProdAssistantsForm(ModelForm):
    class Meta:
        model = ProdAssistants

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(ProdAssistantsForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

class PhotoAssistantsForm(ModelForm):
    class Meta:
        model = PhotoAssistants

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(PhotoAssistantsForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

class HairAssistantsForm(ModelForm):
    class Meta:
        model = HairAssistants

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(HairAssistantsForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

class MakeupAssistantsForm(ModelForm):
    class Meta:
        model = MakeupAssistants

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(MakeupAssistantsForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

class WardrobeAssistantsForm(ModelForm):
    class Meta:
        model = WardrobeAssistants

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(WardrobeAssistantsForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

class ProductionForm(ModelForm):
    class Meta:
        model = Production

    assistants = ModelFieldList(FormField(ProdAssistantsForm))

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(ProductionForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

class PhotoForm(ModelForm):
    class Meta:
        model = Photo

    assistants = ModelFieldList(FormField(PhotoAssistantsForm))

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(PhotoForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

class CateringForm(ModelForm):
    class Meta:
        model = Catering

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(CateringForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

class ArtForm(ModelForm):
    class Meta:
        model = Art

    assistants = ModelFieldList(FormField(ArtAssistantsForm))

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(ArtForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

class MakeupForm(ModelForm):
    class Meta:
        model = Makeup

    assistants = ModelFieldList(FormField(MakeupAssistantsForm))

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(MakeupForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

class HairForm(ModelForm):
    class Meta:
        model = Hair

    assistants = ModelFieldList(FormField(HairAssistantsForm))

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(HairForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

class WardrobeForm(ModelForm):
    class Meta:
        model = Wardrobe

    assistants = ModelFieldList(FormField(WardrobeAssistantsForm))

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(WardrobeForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

class ShootsForm(ModelForm):
    class Meta:
        model = Shoots
        widgets = {
            'notes': TextAreaField(),
        }
        exclude = ['created_by']

    talent = ModelFieldList(FormField(TalentForm))
    photo = ModelFormField(PhotoForm)
    catering = ModelFormField(CateringForm)
    art = ModelFormField(ArtForm)
    makeup = ModelFormField(MakeupForm)
    hair = ModelFormField(HairForm)
    wardrobe = ModelFormField(WardrobeForm)
    production = ModelFormField(ProductionForm)

class ContactForm(Form):
  name = TextField("Name", [validators.Required("Please enter your name.")])
  email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter a valid email address.")])
  submit = SubmitField("Sign Up")

class SignupForm(Form):
  firstname = TextField("First name",  [validators.Required("Please enter your first name.")])
  lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('Password', [validators.Required("Please enter a password.")])
  #companycode = TextField("Company Code",  [validators.Required("Please enter a company sign up code.")])
  submit = SubmitField("Create account")
 
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False   

    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user:
      self.email.errors.append("That email is already taken")
      return False
    else:
      return True

class MyAccountForm(Form):
  firstname = TextField("First name",  [validators.Required("Please enter your first name.")])
  lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  oldpassword = PasswordField('Old Password')
  newpassword = PasswordField('New Password')
  #companycode = TextField("Company Code",  [validators.Required("Please enter a company sign up code.")])
  submit = SubmitField("Save Changes")
 
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False   

    
    user = db.session.query(User).filter_by(email=session['email']).first()
    if user.email != self.email.data.lower():
        userWithNewEmail = User.query.filter_by(email = self.email.data.lower()).first()
        if userWithNewEmail:
          self.email.errors.append("That email is already taken")
          return False

    if len(self.newpassword.data) > 0:
        if user and user.check_password(self.oldpassword.data):
            return True
        else:
            self.oldpassword.errors.append("Old password is invalid")
    
    return True


class SignInForm(Form):
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Sign In")
   
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
 
    def validate(self):
        if not Form.validate(self):
            return False
     
        user = User.query.filter_by(email = self.email.data.lower()).first()
        if user and user.check_password(self.password.data):
            return True
        else:
            self.email.errors.append("Invalid e-mail or password")
            return False

class EmailForm(Form):
    recipient = TextField("Recipients",  [validators.Required("Please enter an email address."), validators.Email("Please enter a valid email address.")])
    cc = TextField("CC",  [validators.Email("Please enter a valid email address.")])
    subject = TextField("Subject", [validators.Required("Please enter a subject.")])
    message = TextField("Body")
    submit = SubmitField("Send")

class ContactForm(Form):
    name = TextField("Name",  [validators.Required("Please enter your name.")])
    email = TextField("Email",  [validators.Required("Please enter an email address."), validators.Email("Please enter a valid email address.")])
    subject= TextField("Subject",  [validators.Required("Please enter a subject.")])
    message = TextField("Message",  [validators.Required("Please enter a message for us.")])