from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_appbuilder.models.mixins import ImageColumn
from flask_appbuilder import Model


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000))
    rarity = db.Column(db.String(10000))
    filename = db.Column(db.String(50))
    price = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    cards = db.relationship('Card')
    currency = db.Column(db.Integer)
    
