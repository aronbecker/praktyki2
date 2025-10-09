from .extensions import db
from datetime import datetime

class Opinion(db.Model):
    __tablename__ = 'opinion'
    id = db.Column(db.BigInteger, primary_key=True)
    rating = db.Column(db.SmallInteger, nullable=False)
    comment = db.Column(db.Text)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'))

    companies = db.relationship('CompanyOpinion', backref='opinion', lazy=True)