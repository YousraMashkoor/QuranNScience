from app import db


class Verification(db.Model):
    __tablename__ = "Verification"
    
    verifyID = db.Column(db.Integer, primary_key=True)
    Verifier1 = db.Column(db.Integer, db.ForeignKey('user.id'))
    Verifier2 = db.Column(db.Integer, db.ForeignKey('user.id'))
    Verifier3 = db.Column(db.Integer, db.ForeignKey('user.id'))
    verifyDate = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(120), nullable=False)# status(pending,underreview,processed)
   
    def __init__(self, Verifier1, Verifier2, Verifier3, verifyDate, status):
        self.Verifier1 = Verifier1
        self.Verifier2 = Verifier2
        self.Verifier3 = Verifier3
        self.verifyDate = verifyDate
        self.status = status
    def tojson(self):
        return {
            "verifyID": self.verifyID,
            "Verifier1": self.Verifier1,
            "Verifier2": self.Verifier2,
            "Verifier3": self.Verifier3,
            "verifyDate": self.verifyDate,
            "status": self.status,
        }
        