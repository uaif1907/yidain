from ..extends import db

class OrdersGoods(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    uid = db.Column(db.Integer,db.ForeignKey('user.uid'))
    oid = db.Column(db.Integer,db.ForeignKey('orders.oid'))
    gid = db.Column(db.Integer,db.ForeignKey('goods.id'))
