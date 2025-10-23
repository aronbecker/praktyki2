from .extensions import db
from datetime import datetime, timezone, timedelta

class Opinion(db.Model):
    __tablename__ = 'opinion'
    id = db.Column(db.BigInteger, primary_key=True)
    rating = db.Column(db.SmallInteger, nullable=False)
    comment = db.Column(db.Text)
    creation_date = db.Column(db.DateTime, default=datetime.now(timezone(timedelta(hours=2))))
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'))
    company_id = db.Column(db.BigInteger, db.ForeignKey('company.id'))

    user = db.relationship('User', lazy=False)

    def toStr(self):
        return {
            "id" : self.id,
            "rating": self.rating,
            "comment": self.comment,
            "creation_date": int(time.mktime(self.creation_date.timetuple())) * 1000,
            "user_name": self.user.firstname + " " + self.user.lastname
        }