from app import db


class Tag(db.Model):
    __tablename__ = "tag"

    id = db.Column(db.Integer, primary_key=True)
    tagName = db.Column(db.String(120), nullable=False)
    tagLink = db.Column(db.String(120), nullable=False)

    # pageId = db.Column(db.Integer, db.ForeignKey('page.id'))

    def __init__(
        self,
        tagName,
        tagLink,
        # pageId,
    ):
        self.tagName=tagName
        self.tagLink=tagLink
        # self.pageId = pageId
