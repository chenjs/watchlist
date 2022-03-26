from flask import Flask, url_for

from watchlist import app, db


@app.route('/home')
def home():
# 	return u'欢迎来到WatchList的世界！'
	return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)

