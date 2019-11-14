from flask_restful import Resource,fields
from ..database.addtable import Add

# 返回资源
class AddListAPI(Resource):
    def get(self):
        """
        :param uid:对应用户id
        :param address:地址

        :return: 返回地址信息
        """
        con = []
        data = Add.query.all()
        for item in data:
            item = item.__dict__
            item.pop('_sa_instance_state')
            con.append(item)
        return {'code':200,'msg':'123','data':con}