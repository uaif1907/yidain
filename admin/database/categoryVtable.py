from ..extends import db


class CategoryValue(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    cpid = db.Column(db.Integer,db.ForeignKey('categories_properties.id'))
    value = db.Column(db.String(20))
    code = db.Column(db.String(20))


