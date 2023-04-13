from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__, static_url_path='',
            static_folder='template', template_folder='template')
# app = Flask(__name__)

app.config.from_pyfile('config/config.py')
app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)
CORS(app, supports_credentials=True)

db = SQLAlchemy()
db.init_app(app)

from src.models import *


# from . import models
with app.app_context():
    db.create_all()
    db.session.commit()
    print('data is created')
    # book = Books.query.all()
