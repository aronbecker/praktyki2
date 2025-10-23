from .extensions import db

companyCategory = db.Table('company_category', 
    db.Column('id', db.BigInteger, primary_key=True),
    db.Column('company_id', db.BigInteger, db.ForeignKey('company.id')),
    db.Column('category_id', db.BigInteger, db.ForeignKey('category.id'))
)
    