from .extends import api
from .apis.user import UserlistAPI

def register_api():
    api.add_resource(UserlistAPI,"/api/user/",endpoint="users")

