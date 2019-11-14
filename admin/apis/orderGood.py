from flask_restful import Resource
from  ..database.ordersGoods import OrdersGoods
from ..database.orderstable import Orders
from ..database.goodstable import Goods


class OrderGoodsAPI(Resource):
    def get(self):
        con = []
        data = OrdersGoods.query.all()
        for item in data:
            item = item.__dict__
            item.pop('_sa_instance_state')
            con.append(item)
        return {'data':str(con)}