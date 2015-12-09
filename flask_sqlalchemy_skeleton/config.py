import os

_basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "mysecretkey"
    TEMPLATE_FOLDER = "templates"
    BCRYPT_LOG_ROUNDS = 12

class DevConfig(object):
    DEBUG = True
    RELOAD = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False