

#wtforms - pip install flask-wtf

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField
from wtforms.validators import DataRequired, Length , Email


class login(FlaskForm):
	uname = StringField('Username or Email',
		validators=[DataRequired(),Length(min = 2, max = 20)])
	pwrd = PasswordField('Enter password',
		validators=[DataRequired(),Length(min = 2)]) #Length(min=8)

	submit = SubmitField('Login')


class register(FlaskForm):
	name = StringField('Enter Name',validators=[DataRequired()])
	uname = StringField('Enter Username',validators=[DataRequired()])
	pwrd = PasswordField('Enter Password',validators=[DataRequired(),Length(min=8)])
	email = EmailField('Enter Email',validators=[DataRequired()])
	submit = SubmitField('Sign up')


