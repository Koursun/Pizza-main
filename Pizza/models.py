from Pizza import db
from sqlalchemy.sql import func

class Customer_Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Interger, nullable=False)
    name = db.Column(db.String(25))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))

class pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    price = db.Column(db.Integer)
    