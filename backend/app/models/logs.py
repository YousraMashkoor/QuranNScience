from app import db


class Logs(db.Model):
    __tablename__ = "Logs"
    
    logId = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date, nullable=False)
    
    action = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), nullable=False) # status(pending,underreview,processed)
    ipaddress = db.Column(db.String(120), nullable=False)
    def __init__(self, user, date, action, description, status, ipaddress):
        self.user = user
        self.date = date
        self.action = action
        self.description = description
        self.status = status
        self.ipaddress = ipaddress
    def tojson(self):
        return {
            "logId": self.logId,
            "user": self.user,
            "date": self.date,
            "action": self.action,
            "description": self.description,
            "status": self.status,
            "ipaddress": self.ipaddress,
        }
    