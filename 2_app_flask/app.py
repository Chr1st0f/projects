#!/opt/rh/rh-python36/root/usr/bin/python
##!../../venv_flask/bin/python
# !--*--coding:utf-8--*--

from db.data import Articles # Import data . Should be replaced by a DB

from flask import Flask, render_template

app = Flask(__name__)

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

if __name__=='__main__':
	app.run(host='0.0.0.0', port='3001', debug=True)
