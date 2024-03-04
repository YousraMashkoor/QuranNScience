from app import db


class RingComposition(db.Model):
    __tablename__ = "ring_composition"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(120), nullable=False)  # ayats or subparts

    # ayatId = db.Column(db.Integer, db.ForeignKey('ayat.id'))
    # pageId = db.Column(db.Integer, db.ForeignKey('page.id'))
    # ringId = db.Column(db.Integer, db.ForeignKey('ring_composition.id'))

    def __init__(
        self,
        type,
        # ayatId,
        # pageId,
        # ringId,
    ):
        self.type = type
        # self.ayatId = ayatId
        # self.pageId = pageId
        # self.ringId = ringId
