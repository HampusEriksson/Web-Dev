from . import db
from sqlalchemy.sql import func
from flask_appbuilder.models.mixins import ImageColumn
from flask_appbuilder import Model


class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000))
    e = db.Column(db.String(10000))
    c = db.Column(db.String(10000))
    a = db.Column(db.String(10000))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    goals = db.relationship('Goal')
    
