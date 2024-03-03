from app import db


class RootWord(db.Model):
    __tablename__ = "root_word"

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(120), nullable=False)
    abjadNumber = db.Column(db.integer(), nullable=False, default=1)
    rootWord = db.Column(db.String(120), nullable=False)
    count = db.Column(db.integer(), nullable=False, default=1)
    countTillAyatStart = db.Column(db.integer(), nullable=False, default=1)
    countTillAyatEnd = db.Column(db.integer(), nullable=False, default=1)
    ayatIndexNumber = db.Column(db.integer(), nullable=False, default=1)

    # ayatId = db.Column(db.Integer, db.ForeignKey('ayat.id'))
    # meaningId = db.Column(db.Integer, db.ForeignKey('meaning.id'))
    # wordId = db.Column(db.Integer, db.ForeignKey('word.id')) # need to make inter middiate table for this
    # verifyId = db.Column(db.Integer, db.ForeignKey('verify.id'))
    # pageId = db.Column(db.Integer, db.ForeignKey('page.id'))

    def __init__(
        self,
        word,
        type,
        abjadNumber,
        rootWord,
        count,
        countTillAyatStart,
        countTillAyatEnd,
        ayatIndexNumber,
        # ayatId,
        # meaningId,
        # wordId,
        # verifyId,
        # pageId,
    ):
        self.word = word
        self.type = type
        self.abjadNumber = abjadNumber
        self.rootWord = rootWord
        self.count = count
        self.countTillAyatStart = countTillAyatStart
        self.countTillAyatEnd = countTillAyatEnd
        self.ayatIndexNumber = ayatIndexNumber
        # self.ayatId = ayatId
        # self.meaningId = meaningId
        # self.wordId = wordId
        # self.verifyId = verifyId
        # self.pageId = pageId