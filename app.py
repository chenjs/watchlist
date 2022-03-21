from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello():
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
	
	

