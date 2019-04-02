#!../../venv_flask/bin/python
# !--*--coding:utf-8--*--

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# Pass parameters to bootstrap class 
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

if __name__=='__main__':
	app.run(debug=True)