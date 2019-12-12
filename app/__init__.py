import random

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(56)

# Database Connection
db_info = {'host': 'localhost',
           'database': 'blog_website',
           # 'psw':' ',
           'user': 'Yulelechka',
           'port': ' '}

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgres://{db_info['user']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TACK_MODIFICATIONS'] = False  # without this line we will receive warnings

# Database Representation
db = SQLAlchemy(app)  # defines Database from the app
migrate = Migrate(app, db)  # apply all changes inside the app

from app import models
from app import routes