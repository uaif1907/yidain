from ..extends import db

class User(db.Model):
    uid = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    name = db.Column(db.String(20))
    reg_time = db.Column(db.TIMESTAMP)
    phone = db.Column(db.Integer)
    idcard = db.Column(db.String(18))
    realname = db.Column(db.String(20))
