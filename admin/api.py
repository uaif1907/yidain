from .extends import api
from .apis.user import UserlistAPI
from .apis.shopcar import ShopcarAPI


def register_api():
    api.add_resource(UserlistAPI,"/api/user/",endpoint="users")
    api.add_resource(ShopcarAPI, "/api/shopcar/", endpoint="shopcar")

