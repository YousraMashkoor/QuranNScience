from app import db


class Ayat(db.Model):
    __tablename__ = "ayat"

    id = db.Column(db.Integer, primary_key=True)
    ayatNumber = db.Column(db.integer(), nullable=False, default=1)
    abjadNumber = db.Column(db.integer(), nullable=False, default=1)
    ayatText = db.Column(db.String(120), nullable=False)
    # surahId = db.Column(db.Integer, db.ForeignKey('surah.id'))
    # meaningId = db.Column(db.Integer, db.ForeignKey('meaning.id'))
    # verifyId = db.Column(db.Integer, db.ForeignKey('verify.id'))
    # pageId = db.Column(db.Integer, db.ForeignKey('page.id'))

    def __init__(
        self,
        ayatNumber,
        abjadNumber,
        ayatText,
        # surahId,
        # meaningId,
        # verifyId,
        # pageId,
        
    ):
        self.ayatNumber = ayatNumber
        self.abjadNumber = abjadNumber
        self.ayatText = ayatText
        # self.surahId = surahId
        # self.meaningId = meaningId
        # self.verifyId = verifyId
        # self.pageId = pageId