from app import db


class Meaning(db.Model):
    __tablename__ = "meaning"

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(120), nullable=False)
    meaningInEnglish = db.Column(db.String(120), nullable=False)
    meaningInUrdu = db.Column(db.String(120), nullable=False, default=1)

    # verifyId = db.Column(db.Integer, db.ForeignKey('verify.id'))

    def __init__(
        self,
        word,
        meaningInEnglish,
        meaningInUrdu,
        # verifyId
    ):
        self.word = word
        self.meaningInEnglish = meaningInEnglish
        self.meaningInUrdu = meaningInUrdu
        # self.verifyId = verifyId
