from app import db
import datetime


class Verification(db.Model):
    __tablename__ = "verification"

    id = db.Column(db.Integer, primary_key=True)
    verifyDate = db.Column(db.Date(), nullable=False, default=datetime.datetime.now())
    status = db.Column(db.String(120), nullable=False)

    # verifierIds = db.Column(db.Integer, db.ForeignKey('user.id')) # need to create intermeddiate table

    def __init__(
        self,
        verifyDate,
        status,
        # verifierIds,
    ):
        self.verifyDate = verifyDate
        self.status = status
        # self.verifierIds = verifierIds
