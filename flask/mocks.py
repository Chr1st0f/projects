from flask import abort
class Post():

	POSTS = [ 
		{ 'id': 1, 'title':'1st post', 'content': 'Content of first post' }, 
		{ 'id': 2, 'title':'2nd post', 'content': 'Content of second post' }, 
		{ 'id': 3, 'title':'3rd post', 'content': 'Content of third post' },
	]

	@classmethod	# call directly Post.all() with no need to create an instance
	def all(cls):
		""" Fetch all posts """
		return cls.POSTS

	@classmethod
	def find(cls, id):
		""" Fetch single post """
		try:
			return cls.POSTS[int(id) - 1]
		except IndexError:
			abort(404)