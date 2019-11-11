from flask_restful import Resource
from flask import request

class GoodsAPI(Resource):
    def get(self):
        return {'data':[2,3]}

    def post(self):
        # dataBack = request.get_json(silent=True)
        # print('first',dataBack)
        print(123,list(request.form)[0])
        return {'data':200}