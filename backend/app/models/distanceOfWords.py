from app import db


class DistanceOfWords(db.Model):
    __tablename__ = "distance_of_words"

    id = db.Column(db.Integer, primary_key=True)
    letterCount = db.Column(db.integer(), nullable=False, default=1)
    wordcount = db.Column(db.integer(), nullable=False, default=1)

    # firstWordId = db.Column(db.Integer, db.ForeignKey('word.id'))
    # secondWordId = db.Column(db.Integer, db.ForeignKey('word.id'))
    # pageId = db.Column(db.Integer, db.ForeignKey('page.id'))

    def __init__(
        self,
        letterCount,
        wordcount,
        # firstWordId,
        # secondWordId,
        # pageId,
    ):
        self.letterCount = letterCount
        self.wordcount = wordcount
        # self.firstWordId=firstWordId
        # self.secondWordId=secondWordId
        # self.pageId=pageId
