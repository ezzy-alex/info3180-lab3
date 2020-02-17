from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import Email,DataRequired

class ContactForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired()])
    subject = StringField("Subject",validators=[DataRequired()])
    msg = TextAreaField("Message",validators=[DataRequired()])