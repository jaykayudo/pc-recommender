from flask import Flask
# from mixins import  login_required
from datetime import timedelta
import os
app = Flask(__name__)
app.secret_key = os.urandom()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(days= 1)