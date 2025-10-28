from .extensions import db

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    companies = db.relationship('Company', secondary='company_category', back_populates="categories")
    keywords = db.relationship('Keyword', backref='category')

    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "keywords": [k.keyword for k in self.keywords]
        }