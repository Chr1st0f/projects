#!../../venv_flask/bin/python
# !--*--coding:utf-8--*--

__author__ = 'Cazin Christophe'

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import abort
# from mocks import Post  # import Post object in mocks.py - used before the sqlite db creation

app = Flask(__name__)
# Use sqlite model
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Table structure composed of id, title, content
class Post(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255))
	content = db.Column(db.Text)
	#created_at = db.Column(db.DateTime, default=db.func.now())
	#updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

	def __repr__(self): # what is printed when I do method on this object
		return '<Post {}>'.format(self.title)


# The following function generate a filter called pluralize into flask filter 
# If the value is 1 it print "1 post" else it prints "x posts" or the second parameter (plural) give the value of plural 
# e.g pluralize(3, 'cheval', 'chevaux' )
@app.context_processor
def utility_processor():
	def pluralize(count, singular, plural=None):
		if not isinstance(count, int):			# isinstance test if count is interger and return True if yes 
			raise ValueError('{} must be an integer'.format(count))
		plural = "{}s".format(singular) if not plural else plural # If plural is not defined then plural = singular+s 
		string = singular if count == 1 else plural
		return "{} {}".format(count, string)
	return dict(pluralize=pluralize)

@app.context_processor
def inject_now():
	return dict(now=datetime.now())

@app.route('/')  # Means when / ( start url ) launch home function
def home():
	return render_template('pages/home.html')

@app.route('/contact') 
def contact():
	return render_template('pages/contact.html')

@app.route('/about')
def about():
	return render_template('pages/about.html')

@app.route('/blog')
def posts_index():
	# posts = Post.all()  # with import mocks.py
	posts = Post.query.all() 
	return render_template('posts/index.html', posts = posts )

@app.route('/blog/posts/<int:id>')
def posts_show(id):
	#post = Post.find(id) # with import mocks.py
	post = Post.query.get(id)

	if not post: # if no answer to DB ( unknown value)
		abort(404)
	return render_template('posts/show.html', post = post )

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

if __name__ == '__main__':
	db.create_all()  # Create the DB only if it does not exist
	app.run(debug=True, port='3000')
