from . import app, db, bcrypt
from flask.ext.login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property



class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(80), unique=True)
    _password = db.Column(db.String(80))

    def __init__(self, email, password):
        self.email = email
        self._set_password(password)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)


db.create_all()