# app.py
 
from flask import Flask
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/library.db'
app.secret_key = "This is the internet!"
app.debug = True

db = SQLAlchemy(app)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('styles.scss', filters='pyscss', output='styles.css')
assets.register('scss_all', scss)