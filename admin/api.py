from .extends import api
from .apis.userApi import UserlistAPI
from .apis.addressApi import AddListAPI


def register_api():
    api.add_resource(UserlistAPI,"/api/user/",endpoint="users")
    api.add_resource(AddListAPI,"/api/add/",endpoint="adds")