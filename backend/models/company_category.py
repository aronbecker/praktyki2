from .extensions import db

class CompanyCategory(db.Model):
    __tablename__ = 'company_category'
    company_id = db.Column(db.BigInteger, db.ForeignKey('company.id'), primary_key=True)
    category_id = db.Column(db.BigInteger, db.ForeignKey('category.id'), primary_key=True)