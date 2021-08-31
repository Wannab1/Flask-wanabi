import os
class Config(object):
    SECRET_KEY = 'my_secret_key'
    
class DevelomentConfig(object):
    DEBUG = True
    PORT = 5000
    SQLALCHEMY_DATABASE_URI =  'mysql+pymysql://root:feoleoas11@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False