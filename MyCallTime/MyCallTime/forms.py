from flask_wtf import Form
from wtforms import StringField, TextAreaField, TextField, SubmitField, ValidationError, validators

class ContactForm(Form):
  name = TextField("Name", [validators.Required("Please enter your name.")])
  email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter a valid email address.")])
  submit = SubmitField("Sign Up")