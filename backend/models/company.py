from .company_category import companyCategory
from .extensions import db

class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(50))
    email = db.Column(db.String(255))
    owner_name = db.Column(db.String(255))
    website_url = db.Column(db.String(255))
    rating = db.Column(db.SMALLINT)
    ratingCount = db.Column(db.Integer)
    nip = db.Column(db.String(10))
    regon = db.Column(db.String(14))

    def __init__(self, name, phone_number, email, owner_name, website_url, nip, regon):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.owner_name = owner_name
        self.website_url = website_url
        self.nip = nip
        self.regon = regon
        self.rating = 0
        self.ratingCount = 0

    def __init__(self):
        pass

    address = db.relationship('Address', back_populates='company', uselist=False)
    categories = db.relationship('Category', secondary=companyCategory)
    opinions = db.relationship('Opinion', backref='company')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone_number': self.phone_number,
            'email': self.email,
            'owner_name': self.owner_name,
            'website_url': self.website_url,
            'rating': self.rating,
            'ratingCount': self.ratingCount,
            'nip': self.nip,
            'regon': self.regon,
            'address': {
                'town': self.address.town,
                'street': self.address.street,
                'buildingNumber': self.address.building_number,
                'apartmentNumber': self.address.apartment_number
            },
            'categories': [c.name for c in self.categories]
        }