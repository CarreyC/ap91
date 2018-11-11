from apple import db

class Banner(db.Model):
    __tablename__ ='banner'
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