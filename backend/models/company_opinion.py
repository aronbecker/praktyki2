from .extensions import db
class CompanyOpinion(db.Model):
    __tablename__ = 'company_opinion'
    company_id = db.Column(db.BigInteger, db.ForeignKey('company.id'), primary_key=True)
    opinion_id = db.Column(db.BigInteger, db.ForeignKey('opinion.id'), primary_key=True)