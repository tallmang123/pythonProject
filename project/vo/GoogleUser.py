from flask_login import UserMixin


class GoogleUser(UserMixin):
    def __init__(self, googleId, name, email, picture):
        self.id = googleId
        self.name = name
        self.email = email
        self.picture = picture

    def as_payload(jsonData):
        return GoogleUser(jsonData['id'], jsonData['name'], jsonData['email'], jsonData['picture'])

    def as_dict(self):
        return self.__dict__
