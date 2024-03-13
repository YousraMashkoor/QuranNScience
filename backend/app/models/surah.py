from app import db


class Surah(db.Model):
    __tablename__ = "surah"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    arabicName = db.Column(db.String(120), nullable=False)
    totalAyat = db.Column(db.Integer, nullable=False, default=1)
    totalLetters = db.Column(db.Integer, nullable=False, default=1)
    abjadNumber = db.Column(db.Integer, nullable=False, default=1)
    # meaningId = db.Column(db.Integer, db.ForeignKey('meaning.id'))
    # meaning = db.relationship("meaning", backref=backref("meaning", uselist=False))
    # verifyId = db.Column(db.Integer, db.ForeignKey('verify.id'))
    # verify = db.relationship("verify", backref=backref("verify", uselist=False))
    # pageId = db.Column(db.Integer, db.ForeignKey('page.id'))
    # page = db.relationship("page", backref=backref("page", uselist=False))

    def __init__(
        self,
        email,
        password,
        username,
        phoneNumber,
        bio,
        type,
        name,
        arabicName,
        totalAyat,
        totalLetters,
        abjadNumber,
        # meaningId,
        # meaning,
        # verifyId,
        # verify,
        # pageId,
        # page,
    ):
        self.email = email
        self.password = password
        self.username = username
        self.username = phoneNumber
        self.bio = bio
        self.type = type
        self.name = name
        self.arabicName = arabicName
        self.totalAyat = totalAyat
        self.totalLetters = totalLetters
        self.abjadNumber = abjadNumber
        # self.meaningId = meaningId
        # self.meaning = meaning
        # self.verifyId = verifyId
        # self.verify = verify
        # self.pageId = pageId
        # self.page = page
    def tojson(self):
        return {
            "id": self.id,
            "name": self.name,
            "arabicName": self.arabicName,
            "totalAyat": self.totalAyat,
            "totalLetters": self.totalLetters,
            "abjadNumber": self.abjadNumber,
            # "meaningId": self.meaningId,
            # "meaning": self.meaning,
            # "verifyId": self.verifyId,
            # "verify": self.verify,
            # "pageId": self.pageId,
            # "page": self.page,
        }