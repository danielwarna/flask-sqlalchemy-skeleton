from flask_sqlalchemy_skeleton import app, db
from flask.ext.login import UserMixin

class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, email, password):
        self.email = email
        self.password = password


db.create_all()