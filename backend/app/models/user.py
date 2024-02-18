from app import db


class Permissions:
    DEFAULT = 0x01
    ADMIN = 0xFF


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    phoneNumber = db.Column(db.String(120), nullable=True)
    bio = db.Column(db.String(120), nullable=True)
    type = db.Column(
        db.Integer, nullable=False, default=Permissions.DEFAULT
    )  # default, admin, hafiz etc.

    def __init__(self, email, password, username, phoneNumber, bio, type):
        self.email = email
        self.password = password
        self.username = username
        self.username = phoneNumber
        self.bio = bio
        self.type = type
