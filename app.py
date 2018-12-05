# app.py
 
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

secret_key = os.environ.get('FLASK_SECRET_KEY')
if not secret_key:
    print('Warning: Secret key environment variable not detected. Do not run in production without it.')
    secret_key = 'Do not use in production without secret key!'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = secret_key
app.debug = True

db = SQLAlchemy(app)
