from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Card, User
from . import db
import json
from base64 import b64encode

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    return render_template("home.html", user=current_user, users = User.query.all())

@views.route('/mycards', methods=['GET', 'POST'])
@login_required
def mycards():

    return render_template("mycards.html", user=current_user)

    

@views.route('/buycards', methods=['GET', 'POST'])
@login_required
def buycards():
    if request.method == 'POST':
        ids = request.form.get('ids')
        print(ids)
        return render_template("buycards.html", user=current_user, users = User.query.all(),   cards = Card.query.all() if ids == "All" else Card.query.filter_by(user_id = ids))

    return render_template("buycards.html", user=current_user, users = User.query.all(),  cards = Card.query.all())


@views.route('/user/<int:param>', methods=['GET', 'POST'])
@login_required
def user(param):

    return render_template("user.html", user = User.query.filter_by(id=param).first())