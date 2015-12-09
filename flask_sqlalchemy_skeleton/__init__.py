from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt

import config

app = Flask(__name__)
app.config.from_object(config.DevConfig)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

import models
import routes
import errors


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    user = models.User.query.filter(id="user_id").first()
    return user