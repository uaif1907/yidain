from ..extends import db

class Add(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    address = db.Column(db.String(30))

