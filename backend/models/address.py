from .extensions import db

class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.BigInteger, primary_key=True)
    town = db.Column(db.String(255), nullable=False)
    street = db.Column(db.String(255))
    building_number = db.Column(db.String(50))
    apartment_number = db.Column(db.SmallInteger)

    companies = db.relationship('Company', backref='address', lazy=True)