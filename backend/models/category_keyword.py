from .extensions import db


class CategoryKeyWord(db.Model):
    __tablename__ = 'category_keyword'
    category_id = db.Column(db.BigInteger, db.ForeignKey('category.id'), primary_key=True)
    keyword_id = db.Column(db.BigInteger, db.ForeignKey('keyword.id'), primary_key=True)
