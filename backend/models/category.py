from .extensions import db

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    companies = db.relationship('CompanyCategory', backref='category', lazy=True)
    keywords = db.relationship('CategoryKeyWord', backref='category', lazy=True)