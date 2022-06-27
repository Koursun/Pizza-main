from Pizza import db
from sqlalchemy.sql import func

class customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    active = db.Column(db.Boolean, nullable=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=True)
    def __repr__(self):
        return self.name
# make jess specials
class pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    price = db.Column(db.Integer)
    

