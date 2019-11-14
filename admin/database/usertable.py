from ..extends import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20)) # 用户名
    password = db.Column(db.String(20)) # 密码
    name = db.Column(db.String(20))     # 昵称
    reg_time = db.Column(db.TIMESTAMP)  # 注册时间
    idcard = db.Column(db.String(18))   # 实名认证
    realname = db.Column(db.String(20)) # 姓名
    sex = db.Column(db.Integer)         # 性别
    age = db.Column(db.Integer)         # 年龄
    phone = db.Column(db.String(11))    # 手机号
    # aid = db.Column(db.Integer)         # 住址



