from flask_wtf import Form
from wtforms import StringField, TextAreaField, TextField, SubmitField, ValidationError, validators, PasswordField
from MyCallTime.models import db, User, Shoots, Talent
from wtforms_alchemy import ModelForm, model_form_factory, ModelFieldList
from wtforms.fields import FormField

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

class ShootsForm(ModelForm):
    class Meta:
        model = Shoots
        exclude = ['created_by']

    talent = ModelFieldList(FormField(TalentForm))


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