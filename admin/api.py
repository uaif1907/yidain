from .extends import api
from .apis.user import UserlistAPI
from .apis.goods import GoodsAPI
from .apis.ordersApi import OrdersAPI
def register_api():
    api.add_resource(UserlistAPI,"/api/user/",endpoint="users")
    api.add_resource(OrdersAPI, "/api/orders/", endpoint="orders")
    api.add_resource(GoodsAPI, "/api/goods", endpoint="first")





