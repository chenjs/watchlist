from flask import Flask, session, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import sys
import click

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////" + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
	"""Initialize the database."""
	if drop:
		db.drop_all()
	db.create_all()
	click.echo('Initialized database.')


@app.cli.command()
def forge():
	"""Generate fake data."""
	db.create_all()

	name = "Tom Chen"
	movies = [
		{'title' : 'My Neighbor Totoro', 'year':1988},
		{'title': 'Dead Poets Society', 'year': '1989'},
		{'title': 'A Perfect World', 'year': '1993'},
		{'title': 'Leon', 'year': '1994'},
		{'title': 'Mahjong', 'year': '1996'},
		{'title': 'Swallowtail Butterfly', 'year': '1996'},
		{'title': 'King of Comedy', 'year': '1999'},
		{'title': 'Devils on the Doorstep', 'year': '1999'},
		{'title': 'WALL-E', 'year': '2008'},
		{'title': 'The Pork of Music', 'year': '2012'}
	]

	user = User(name=name)
	db.session.add(user)
	for m in movies:
		movie = Movie(title=m['title'], year=m['year'])
		db.session.add(movie)
	db.session.commit()
	click.echo('Done.')


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))

class Movie(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(60))
	year = db.Column(db.String(4))


@app.route('/')
def index():
	# return render_template('index.html', name=name, movies=movies)
	movies = Movie.query.all()
	return render_template('index.html', movies=movies)
	

@app.route('/home')
def home():
# 	return 'Welcome to My Watchlist Demo'
# 	return u'欢迎来到WatchList的世界！'
	return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
	
@app.route('/user/<name>')
def user(name):
	return "Hello %s" % name

@app.route('/test')
def test_url_for():
	print(url_for('hello'))
	
	print(url_for('user', name='chenjs'))
	
	print(url_for('user', name='peter'))
	
	print(url_for('test_url_for'))
	
	print(url_for('test_url_for', num=2))
	
	return 'test_page'
	
@app.context_processor
def inject_user():
	current_user = User.query.first()
	return dict(user=current_user)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

	

	

