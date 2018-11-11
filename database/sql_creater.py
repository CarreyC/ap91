from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b64aad672fb40002c716d42ad4633db7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@mysql:3306/ap91'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


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

class Banner(db.Model):
    __tablename__ = 'banner'
    id = db.Column(db.Integer, primary_key=True)
    pic = db.Column(db.String(90))
    desc = db.Column(db.String(120))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    pic = db.Column(db.String(30))
    desc = db.Column(db.String(90))
    sub = db.relationship('CateSub', backref='main_category', lazy=True)

class CateSub(db.Model):
    __tablename__ = 'cate_sub'
    id = db.Column(db.Integer, primary_key=True)
    cate_main = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False) # 主要分類
    cate_sub = db.Column(db.Integer) # 次要分類
    item_name = db.Column(db.String(60)) # 產品名稱
    item_pic = db.Column(db.String(60)) # 圖片名稱
    item_desc = db.Column(db.String(60)) # 產品說明


if __name__ == '__main__':
    manager.run()
