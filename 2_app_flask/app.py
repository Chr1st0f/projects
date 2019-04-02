#!/opt/rh/rh-python36/root/usr/bin/python
##!../../venv_flask/bin/python
# !--*--coding:utf-8--*--

from db.data import Articles # Import data . Should be replaced by a DB

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flaskext.MySQL import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.secret_key = 'secret'

# Config Mysql
app.config['MYSQL_DATABASE_HOST'] = 'c_flaskdb'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 't00r'
app.config['MYSQL_DATABASE_DB'] = 'myflaskapp'
app.config['MYSQL_DATABASE_CURSORCLASS'] = 'DictCursor' # Put the result in a dictionnary

# Initialize Mysql
mysql = MySQL()
mysql.init_app(app)

Articles = Articles()  # The functions imported from data.py called Articles will return the content of object artciles 
@app.route('/')
def index(): 
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/articles')
def articles():
	return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
	return render_template('article.html', id = id)

@app.errorhandler(404)
def page_not_found(error):
	return render_template('errors/404.html'), 404

class RegisterForm(Form):
	name = StringField('Name', [validators.Length(min=1, max=50)])
	username = StringField('Username', [validators.Length(min=4, max=25)])
	email = StringField('Email', [validators.Length(min=6, max=50)])
	password = PasswordField('Password', [
		validators.DataRequired(),
		validators.EqualTo('confirm', message='Passwords do not match')
		])
	confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
	# We are usin WTform for registration
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		name = form.name.data
		email = form.email.data
		username = form.username.data
		password = sha256_crypt.encrypt(str(form.password.data))

		# Open a new connection to the DB
		conn = mysql.connect()
		# Create the cursor on this conn object
		cursor = conn.cursor()
		# Execute query
		query = "INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)"
		cursor.execute(query, (name, email, username, password))
		conn.commit() # Commit to DB
		cursor.close() # Close the connection 

		flash('You are now registered and can log in', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', form = form)
# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		# Get Form fields
#		username = request.form('username')
		# password_candidate = request.form('password')
		# Open a new connection to the DB
		conn = mysql.connect()
		# Create the cursor on this conn object
		cursor = conn.cursor()		# Get user by username
		query = "SELECT * FROM users WHERE username = %s"
		result = cursor.execute(query, ["totof"])

		if result > 0:
			# Get stored hash
			data = cursor.fetchone()
			password= data('password')

			# Compare the password
			if sha256_crypt.verify(password_candidate,password):
				app.logger.info('PASSWORD MATCHED')
			else:
				app.logger.info('PASSWORD NOT MATCHED')

		else:
				app.logger.info('NO USER')


	return render_template('login.html')

if __name__=='__main__':
	app.run(host='0.0.0.0', port='3001', debug=True)

