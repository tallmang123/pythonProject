from app import db
import datetime

#use sqlalchemy
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

    def as_dict(self):
        dict = {}
        for c in self.__table__.columns:
            dict[c.name] = getattr(self, c.name)
            if isinstance(dict[c.name], datetime.datetime): # convert type datetime to string
                dict[c.name] = dict[c.name].strftime('%Y-%m-%d %H:%M:%S')
        return dict
        #return {c.name: getattr(self, c.name) for c in self.__table__.columns}


