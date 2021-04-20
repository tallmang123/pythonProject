from app import db


class Account(db.Model):
    __tablename__ = 'account'
    Seq = db.Column(db.Integer, primary_key=True)
    Id = db.Column(db.String(20))
    Password = db.Column(db.String(64))
    Salt = db.Column(db.String(3))
    Status = db.Column(db.String(1))
    AddTime = db.Column(db.DateTime)

    def __init__(self, id, password, salt, status, addtime):
        self.Id = id
        self.Password = password
        self.Salt = salt,
        self.Status = status,
        self.AddTime = addtime


