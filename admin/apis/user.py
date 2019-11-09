from flask_restful import Resource

class UserlistAPI(Resource):
    def get(self):
        return {'data':[1,2,3,4,5]}