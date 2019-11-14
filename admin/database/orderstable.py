from ..extends import db
from sqlalchemy.orm import relationship

class Orders(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    oid = db.Column(db.Integer) # 订单号
    uid = db.Column(db.Integer,db.ForeignKey('user.uid'))   # 用户id
    # aid = db.Column(db.Integer,db.ForeignKey('add.id'))    #收货地址
    status = db.Column(db.Integer) # 订单状态 （1.支付中2.代发货3.运输中4.已签收）
    sid = db.Column(db.Integer,db.ForeignKey('shopcar.id')) #购物车id
    pay = db.Column(db.String(30)) # 支付方式
    time = db.Column(db.String(100)) # 下单时间（生成订单时）
