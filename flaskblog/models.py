from datetime import datetime

from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True, nullable=False)
    email = db.Column('email', db.String(120), unique=True, nullable=False)
    image_file = db.Column('image file', db.String(20), nullable=False, default='default.jpg')
    password = db.Column('password', db.String(60), nullable=False)
    #  relationship
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column('user id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column('title', db.String(20), nullable=False)
    date_posted = db.Column('date posted', db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column('content', db.Text, nullable=False)

    def __repr__(self):

        return f"User('{self.title}', '{self.date_posted}')"
