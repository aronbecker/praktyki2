from .extensions import db

class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(50))
    email = db.Column(db.String(255))
    owner_name = db.Column(db.String(255))
    website_url = db.Column(db.String(255))
    address_id = db.Column(db.BigInteger, db.ForeignKey('address.id'))

    categories = db.relationship('CompanyCategory', backref='company', lazy=True)
    opinions = db.relationship('CompanyOpinion', backref='company', lazy=True)