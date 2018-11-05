from apple import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_uesr(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    realname = db.Column(db.String(30))
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(30), unique=True)
    sex = db.Column(db.String(10))
    facebook = db.Column(db.String(60), unique=True)
    lineid = db.Column(db.String(60), unique=True)
    registe_date = db.Column(db.DateTime, default=datetime.now())