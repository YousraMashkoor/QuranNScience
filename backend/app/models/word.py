from app import db


class Word(db.Model):
    __tablename__ = "word"

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(120), nullable=False)
    abjadNumber = db.Column(db.integer(), nullable=False, default=1)
    linkedWord = db.Column(db.String(120), nullable=False, default=1)
    totalLetters = db.Column(db.integer(), nullable=False, default=1)

    # ayatID = db.Column(db.Integer, db.ForeignKey('ayat.id'))
    # meaningId = db.Column(db.Integer, db.ForeignKey('meaning.id'))
    # rootWordId = db.Column(db.Integer, db.ForeignKey('rootWord.id'))
    # verifyId = db.Column(db.Integer, db.ForeignKey('verify.id'))
    # pageId = db.Column(db.Integer, db.ForeignKey('page.id'))

    def __init__(
        self,
        word,
        type,
        abjadNumber,
        linkedWord,
        totalLetters,
        # ayatID,
        # meaningId,
        # rootWordId,
        # verifyId,
        # pageId,
        
    ):
        self.word=word
        self.type=type
        self.abjadNumber=abjadNumber
        self.linkedWord=linkedWord
        self.totalLetters=totalLetters
        # self.ayatID=ayatID
        # self.meaningId=meaningId
        # self.rootWordId=rootWordId
        # self.verifyId=verifyId
        # self.pageId=pageId