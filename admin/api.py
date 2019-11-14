from .extends import api
<<<<<<< HEAD
from .apis.userApi import UserlistAPI
from .apis.addressApi import AddListAPI
=======
from .apis.user import UserlistAPI
from .apis.shopcar import ShopcarAPI
from .apis.goods import GoodsAPI
>>>>>>> 26921f09a8f2753bcb2772d94c421b9667793a84


def register_api():
    api.add_resource(UserlistAPI,"/api/user/",endpoint="users")
<<<<<<< HEAD
    api.add_resource(AddListAPI,"/api/add/",endpoint="adds")
=======
    api.add_resource(GoodsAPI,"/api/goods",endpoint="first")
    api.add_resource(ShopcarAPI, "/api/shopcar/", endpoint="shopcar")


>>>>>>> 26921f09a8f2753bcb2772d94c421b9667793a84
