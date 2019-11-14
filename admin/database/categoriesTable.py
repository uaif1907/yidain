from ..extends import db

class Categories(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    parent_code = db.Column(db.Integer)
    isend = db.Column(db.Integer)
