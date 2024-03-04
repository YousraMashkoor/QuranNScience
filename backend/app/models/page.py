from app import db


class Page(db.Model):
    __tablename__ = "page"

    id = db.Column(db.Integer, primary_key=True)
    pageLink = db.Column(db.String(120), nullable=False)
    pageIndex = db.Column(db.integer(), nullable=False, default=1)

    # posterId = db.Column(db.Integer, db.ForeignKey('user.id'))
    # verifyId = db.Column(db.Integer, db.ForeignKey('verify.id'))

    def __init__(
        self,
        pageLink,
        pageIndex,
        # posterId,
        # verifyId
    ):
        self.pageLink=pageLink
        self.pageIndex=pageIndex
        # self.posterId = posterId
        # self.verifyId = postverifyIderId
