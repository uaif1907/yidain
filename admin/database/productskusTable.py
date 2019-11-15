from ..extends import db


class Productskus(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    gid = db.Column(db.Integer,db.ForeignKey('goods.id'))
    skuid = db.Column(db.Integer)
    price = db.Column(db.Integer)
    stock = db.Column(db.Integer)
