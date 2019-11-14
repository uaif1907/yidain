from flask_restful import Resource
from ..database.usertable import User
from flask import request



# 时间函数
def EditTime(item):
    item['reg_time'] = item['reg_time'].strftime("%Y-%m-%d %H:%M:%S")
    return item

# 转换性别函数
def Sexchange(item):
    if item['sex'] == 1:
        item['sex'] = '男'
    elif item['sex']  == 0:
        item['sex'] = '女'
    return item

# 返回资源
class UserlistAPI(Resource):
    def get(self):
        """
        获取用户信息
        :param username:用户名
        :param password:密码
        :param name:昵称
        :param reg_time:注册时间
        :param idcard:实名认证
        :param realname:姓名
        :param sex:性别
        :param age:年龄
        :param add:住址
        :param phone:手机号

        :return:返回此表所有信息
        """
        con = []
        data = User.query.all()
        for item in data:
            item = item.__dict__
            item.pop('_sa_instance_state')
            arr = Sexchange(EditTime(item))
            con.append(arr)
        print(con)

        return {'code':200,'msg':'ok','data':con}

    # 添加
    def post(self):
        data = request.form
        username = data['username']
        password = data['password']
        name = data['name']
        reg_time = data['reg_time']
        idcard = data['idcard']
        realname = data['realname']
        sex = data['sex']
        age = data['age']
        phone = data['phone']
        res = User(username=username,password=password,name=name,reg_time=reg_time,idcard=idcard,realname=realname,sex=sex,age=age,phone=phone)
        User.query.session.add(res)
        User.query.session.commit()
        return {'code':200,'msg':'ok','data':str(res)}


    # 删除
    def delete(self):
        # dele = User.query.get(3)
        # User.query.session.delete(dele)
        # User.query.session.commit()
        data = User.query.filter(User.id).all()
        print(data)
        return {'code':200,'msg':'删除成功'}
