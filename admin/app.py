from flask import Flask
from .extends import app_extend,db
from .api import register_api
# 创建flask应用
def create_app():
    app = Flask(__name__)
    app.config.from_object("config")
    register_api()
    # 连接所有扩展
    app_extend(app)
    with app.app_context():
        db.create_all()

    return app

