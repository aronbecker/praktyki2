from .extensions import db

class Keyword(db.Model):
    __tablename__ = 'keyword'
    id = db.Column(db.BigInteger, primary_key=True)
    keyword = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.BigInteger, db.ForeignKey('category.id'))
