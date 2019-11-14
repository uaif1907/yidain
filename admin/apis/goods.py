from flask_restful import Resource
from flask import request,jsonify
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
        return jsonify({'data':str(con).replace('"','').replace('[','').replace(']','')})

    def post(self):
        cat2 = CategoriesProperties.query.filter(CategoriesProperties.cid == '2').first() #类目表动态获取
        cat2.__dict__.pop('_sa_instance_state')
        print(cat2.__dict__)

        cat3 = CategoryValue.query.filter(CategoryValue.cpid == '1').first() #类目属性值动态获取
        cat3.__dict__.pop('_sa_instance_state')
        print(cat3.__dict__)

        data = Goods.query.filter(Goods.cid == '1').first() #商品属性
        data.__dict__.pop('_sa_instance_state')
        print(data.__dict__)

        # 添加
        cid = request.form['cid']
        new = request.form['new']
        name = request.form['name']
        describe = request.form['describe']
        img = request.form['img']
        addgoods = Goods(cid=cid, new=new, name=name,describe=describe, img=img, time=datetime.now())
        Goods.query.session.add(addgoods)
        # 事物
        Goods.query.session.commit()

        # 删除
        deletes = Goods.query.filter(Goods.id == '2').first()
        Goods.query.session.delete(deletes)
        Goods.query.session.commit()

        # 修改
        data1 = Goods.query.filter(Goods.cid == '1').first()
        data1.name = '啦啦啦'
        Goods.query.session.commit()


        return {'data':200}


