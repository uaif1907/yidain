from flask_restful import Resource,fields,request
from admin.database.shopcartable import Shopcar
from flask import jsonify,json
from ..extends import db



shopcar_fields ={
    "id":fields.Integer,
    "uid":fields.Integer,
    "name":fields.String,
    "describe":fields.String,
    "price":fields.Integer,
    "color":fields.String,
    "size":fields.String,
    "total":fields.String,
}



class ShopcarAPI(Resource):
    #获取数据
    def get(self):
        """
        :param uid 用户id
        :param pid 库存id
        :param name 商品名
        :param describe 描述
        :param price 价格
        :param color 颜色
        :param size 尺码
        :param total 总价
        :return: data
        """
        data = Shopcar.query.all()
        con = []
        print(type(data))
        for i in data:
            data = i.__dict__
            con.append(data.pop("_sa_instance_state"))
            print(data)
            # print(i.id,i.uid,i.pid,i.total)
        return {'data': data}

    #删除
    def delete(self):
        # shopcar2 = Shopcar.query.get(3)
        # print(shopcar2)

        # index = request.get_json(silent=True)
        # print(index)
        # shopcar2 = Shopcar.query.filter_by(id==index['3']).all()
        # print(shopcar2)

        index = Shopcar.query.filter(Shopcar.id == '3').all()
        print(index)
        Shopcar.query.session.delete(index)
        Shopcar.que0ry.session.commit()


    #添加接收
    def post(self):
        data = request.form
        uid = data['uid']
        pid = data['pid']
        # name = data['name']
        # describe = data['describe']
        # price = data['price']
        # size = data['size']
        total = data['total']
        res = Shopcar(uid=uid,pid=pid,total=total)
        print(res)
        Shopcar.query.session.add(res)
        Shopcar.query.session.commit()
        return {'code':200,'msg':"添加成功",'data':'res'}








