#!/opt/rh/rh-python36/root/usr/bin/python
##!../../venv_flask/bin/python
# !--*--coding:utf-8--*--

# Declaration part #####################################
from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
import flask_sqlalchemy
# Mysql logging informations
host_mysql = 'c_flaskdb'
db_mysql = 'myflaskapp2'
user_mysql = 'root'
pass_mysql = 't00r'

# Main #################################################

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{}:{}@{}/{}".format(user_mysql,pass_mysql,host_mysql,db_mysql)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:t00r@c_flaskdb/myflaskapp2".format(user_mysql,pass_mysql,host_mysql,db_mysql)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # No track modifications 
app.config['SQLALCHEMY_ECHO'] = True # To log activity in the console

db = SQLAlchemy(app) 

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique = True)
	email = db.Column(db.String(80), unique = True)

	def __init__(self, usename, email):
		self.username = username
		self.email = email

@app.route('/')
def index():
	return render_template('index.html')

if __name__=='__main__':
	app.run(host='0.0.0.0', port='3002', debug=True)