from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import datetime
db = SQLAlchemy()

class User(db.Model):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(255))
    create_date = db.Column(db.DateTime, default = datetime.datetime.now)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.__create_password(password)
    
    def __create_password(self, password):
        return generate_password_hash(password).decode('uft-8')
    def verify_password(self, password):
        r = check_password_hash(self.password, password)
        print(r)
    
        return r
        
