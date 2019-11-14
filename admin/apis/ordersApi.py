from flask_restful import Resource
from flask import request
from ..database.orderstable import Orders
from ..database.shopcartable import Shopcar
from ..database.usertable import User
from _datetime import datetime
from ..extends import db
class OrdersAPI(Resource):
    def get(self):
        con = []
        data = Orders.query.all()
        for item in data:
            item = item.__dict__
            item.pop('_sa_instance_state')
            money = (Shopcar.query.filter(Shopcar.id == item['sid']).first()).total
            name = (User.query.filter(User.uid == item['uid']).first()).name
            phone = (User.query.filter(User.uid == item['uid']).first()).phone
            item.update({'money': money, 'name': name, 'phone': phone})
            con.append(item)
        return {'data':str(con)}
    # def post(self):
    #     data = request.form
    #     print(data)
    #     data1 = Orders(oid = request.form['oid'],uid = request.form['uid'], aid = request.form['aid'],phone = request.form['phone'],status = request.form['money'],pay = request.form['pay'],time=request.form['time'])
    #     print(data1)
    #     Orders.query.session.add(data1)
    #     Orders.query.session.commit()
    #     return {'code':200,'msg':'添加成功','data':'res'}
    # def delete(self):
    #     data = Orders.query.filter(Orders.id=='1').first()
    #     Orders.query.session.delete(data)
    #     Orders.query.session.commit()
    #     return {'code': 200, 'msg': '删除成功', 'data': 'res'}
    # def patch(self):
    #     data = Orders.query.filter(Orders.id==id).first()
    #     data1 = Orders(oid=request.form['oid'], uid=request.form['uid'], aid=request.form['aid'],phone=request.form['phone'], status=request.form['money'], pay=request.form['pay'],time=request.form['time'])
    #     Orders.query.session.commit()
    #     return {'code': 200, 'msg': '修改成功', 'data': 'res'}

