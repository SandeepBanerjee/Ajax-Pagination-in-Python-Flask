from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/pagination'
app.config['SECRET_KEY'] = 'ValarMorgulis'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')

db = SQLAlchemy(app)

from main.product import routes