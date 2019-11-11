from ..extends import db

class Orders(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    oid = db.Column(db.Integer)
    uid = db.Column(db.Integer,db.ForeignKey('user.uid'))   # 用户id
    aid = db.Column(db.String(200))    #收货地址
    phone = db.Column(db.Integer)   # 联系方式
    status = db.Column(db.Integer) # 订单状态 （1.支付中2.代发货3.运输中4.已签收）
    money = db.Column(db.String(100)) # 消费金额
    pay = db.Column(db.String(30)) # 支付方式
    time = db.Column(db.TIMESTAMP) # 下单时间（生成订单时）