from .extensions import db

class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(50))
    email = db.Column(db.String(255))
    owner_name = db.Column(db.String(255))
    website_url = db.Column(db.String(255))
    rating = db.Column(db.SMALLINT, default=0)

    def __init__(self, name, phone_number, email, owner_name, website_url):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.owner_name = owner_name
        self.website_url = website_url

    address = db.relationship('Address', back_populates='company', uselist=False,  lazy=False)
    categories = db.relationship('Category', secondary='company_category', backref='company', lazy=True)
    opinions = db.relationship('CompanyOpinion', backref='company', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone_number': self.phone_number,
            'email': self.email,
            'owner_name': self.owner_name,
            'website_url': self.website_url,
            'rating': self.rating,
            'address': {
                'town': self.address.town,
                'street': self.address.street,
                'buildingNumber': self.address.building_number,
                'apartmentNumber': self.address.apartment_number
            },
        }