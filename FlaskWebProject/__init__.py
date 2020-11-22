"""
The flask application package.
"""
import logging
from flask import Flask
import sys
from werkzeug.contrib.fixers import ProxyFix
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
app.logger.warning('User has failed to log in the application')
Session(app)
db = SQLAlchemy(app)
handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.DEBUG)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
app.logger.addHandler(handler)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views