from models import Opinion, Company
from models import db

def calculateCompanyRating(company_id: int):
    company: Company = Company.query.filter_by(id=company_id).first()
    opinions = Opinion.query.filter(Opinion.company.has(id=company_id)).all()
    
    opinionsCount = len(opinions)
    total = 0
    for o in opinions:
        total += o.rating

    company.rating = total // opinionsCount

    db.session.commit()

