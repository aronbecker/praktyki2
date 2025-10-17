from .extensions import db

class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.BigInteger, primary_key=True)
    town = db.Column(db.String(255), nullable=False)
    street = db.Column(db.String(255))
    building_number = db.Column(db.String(50))
    apartment_number = db.Column(db.SmallInteger)

    company_id = db.Column(db.BigInteger, db.ForeignKey('company.id'), unique=True)
    company = db.relationship('Company', back_populates='address')

    def __init__(self, town, street=None, building_number=None, apartment_number=None):
        self.town = town
        self.street = street
        self.building_number = building_number
        self.apartment_number = apartment_number