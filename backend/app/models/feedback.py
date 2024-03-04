from app import db


class Feedback(db.Model):
    __tablename__ = "feedback"

    id = db.Column(db.Integer, primary_key=True)
    report = db.Column(db.String(120), nullable=False)

    # userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    # pageId = db.Column(db.Integer, db.ForeignKey('page.id'))

    def __init__(
        self,
        report,
        # userId,
        # pageId,
    ):
        self.report=report
        # self.userId = userId
        # self.pageId = pageId
