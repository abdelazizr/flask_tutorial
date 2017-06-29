from app import db

#create a user table
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index=True, unique = True)
    #adding a post fields in the user table.
    posts = db.relationship('Post', backref='author', lazy='dynamic')


# Way to print object content
    def __rep__(self):
        return("<User %r>" % (self.nickname))

#create a Post table.
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # introduce ForeignKey id from User table

    # print posts
    def __repr__(self):
        return '<Post %r>' % (self.body)
