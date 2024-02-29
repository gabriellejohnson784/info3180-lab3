from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Full Name', validators=[InputRequired("Please enter your full name")])
    email_address = StringField('Email', validators=[InputRequired("Please enter your e-mail address"), Email("Please enter a valid e-mail address")])
    subject = StringField('Subject', validators=[InputRequired("Please enter the subject for your message")])
    message= TextAreaField('Message', validators=[InputRequired("Please enter the message you would like to send")])
    button = SubmitField('Send')
