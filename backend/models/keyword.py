from .extensions import db

class KeyWord(db.Model):
    __tablename__ = 'keyword'
    id = db.Column(db.BigInteger, primary_key=True)
    keyword = db.Column(db.String(255), nullable=False)

    categories = db.relationship('CategoryKeyWord', backref='keyword', lazy=True)