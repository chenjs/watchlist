import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////" + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'fdajfsdjfa'

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
	user = User.query.get(int(user_id))
	return user

@app.context_processor
def inject_user():
	current_user = User.query.first()
	return dict(user=current_user)

from watchlist import views, errors, commands
from watchlist.models import User, Movie


