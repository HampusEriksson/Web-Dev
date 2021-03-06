from flask import Blueprint, render_template, request, flash, jsonify
from .models import Course, Goal
from . import db
import json
from base64 import b64encode

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():

    return render_template("home.html")

    

@views.route('/<int:param>', methods=['GET', 'POST'])
def course(param):

    return render_template("course.html", course = Course.query.filter_by(id=param).first())