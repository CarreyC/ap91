from apple import db

class Banner(db.Model):
    __tablename__ ='banner'
    id = db.Column(db.Integer, primary_key=True)
    pic = db.Column(db.String(90))
    desc = db.Column(db.String(120))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
