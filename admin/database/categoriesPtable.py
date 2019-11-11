from ..extends import db

class CategoriesProperties(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    cid = db.Column(db.Integer,db.ForeignKey('categories.id'))
    name = db.Column(db.String(50))
    order = db.Column(db.String(10))