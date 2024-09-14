from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, \
    RadioField, SelectField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField("Name of Students", validators=[DataRequired()])
    Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField('Address')

    email = StringField('Email', validators=[DataRequired(), Email()])

    Age = IntegerField('Age')
    language = SelectField('Language', choices=[('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField('Send')