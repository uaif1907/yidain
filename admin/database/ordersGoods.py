from ..extends import db
from sqlalchemy.orm import relationship
class OrdersGoods(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    uid = db.Column(db.Integer,db.ForeignKey('user.uid'))
    oid = db.Column(db.Integer,db.ForeignKey('orders.id'))
    gid = db.Column(db.Integer,db.ForeignKey('goods.id'))
    ord = relationship('orders',foreign_keys=oid)