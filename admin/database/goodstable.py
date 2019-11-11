from ..extends import db


class Goods(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    cid = db.Column(db.Integer,db.ForeignKey('categories.id'))
    new = db.Column(db.Integer)
    name = db.Column(db.String(20))
    img = db.Column(db.String(100))
    time = db.Column(db.TIMESTAMP)

