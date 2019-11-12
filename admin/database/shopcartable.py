from ..extends import db
from sqlalchemy import ForeignKey

class Shopcar(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    uid = db.Column(db.Integer)
    pid = db.Column(db.Integer)
    total = db.Column(db.String(10))


