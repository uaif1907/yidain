from flask_restful import Resource
from flask import request
from datetime import datetime

from ..database.categoriesTable import Categories
from ..database.categoriesPtable import CategoriesProperties
from ..database.categoryVtable import CategoryValue
from ..database.goodstable import Goods
class GoodsAPI(Resource):
    def get(self):
        con = []
        data = Goods.query.all()
        for item in data:
            ite = item.__dict__
            ite.pop('_sa_instance_state')
            con.append(ite)

        print(con)
        return {'data':str(con)}

    def post(self):
        cat2 = CategoriesProperties.query.filter(CategoriesProperties.cid == '2').first() #类目表动态获取
        cat2.__dict__.pop('_sa_instance_state')
        print(cat2.__dict__)

        cat3 = CategoryValue.query.filter(CategoriesProperties.cid == '2').first() #类目属性值动态获取
        cat3.__dict__.pop('_sa_instance_state')
        print(cat3.__dict__)

        data = Goods.query.filter(CategoriesProperties.cid == '2').first() #商品属性
        # data[0].__dict__.pop('_sa_instance_state')
        # print(data[0].__dict__)
        # print(123,list(request.form)[0])

        # print(request.form['cid'])
        # 添加
        cid = request.form['cid']
        new = request.form['new']
        name = request.form['name']
        img = request.form['img']
        addgoods = Goods(cid=cid,new=new,name=name,img=img,time=datetime.now())
        print(addgoods)
        Goods.query.session.add(addgoods)
        # 事物
        Goods.query.session.commit()
        return {'code':123,'msg':'aa','data':'addgoods'}

    def Goodsdelete(self):
        pass
