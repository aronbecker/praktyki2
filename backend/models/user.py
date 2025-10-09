from .extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    opinions = db.relationship('Opinion', backref='user', lazy=True)