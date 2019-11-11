from flask_restful import Resource

class OrdersAPI(Resource):
    def get(self):
        return {'data':[1,2,3,4,5]}