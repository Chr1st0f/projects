#!../../venv_flask/bin/python
# !--*--coding:utf-8--*--

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, NoneOf   # Verifiy long of field

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blablabla'

class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(), Email(message="Pas bon le username")])
	password = PasswordField('password', validators=[
		InputRequired(), 
		NoneOf(['password','secret','totof'], message='This password is not allowed'),
		Length(min=3, max=15, message="You have to enter at least 3 until 15 characters for this field")
		])


@app.route('/', methods=['GET', 'POST'])
def index():
	form = LoginForm() # Load class for the form
	if form.validate_on_submit():  # If we have click on submit button ( all the field has returned True )
		return 'Form successfully submitted!'
	return render_template('index.html', form=form) # Pass te form to the template

if __name__=='__main__':
	app.run(debug=True)
