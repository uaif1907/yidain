from flask import Flask
from .extends import app_extend,db
from .database.usertable import User

# 创建flask应用
def create_app():
    app = Flask(__name__)
    app.config.from_object("config")
    # 连接所有扩展
    app_extend(app)
    with app.app_context():
        db.create_all()



    return app
