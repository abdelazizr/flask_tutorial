from app import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index=True, unique = True)


# Way to print object content
    def __rep__(self):
        return("<User %r>" % (self.nickname))
