from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Card
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    return render_template("home.html", user=current_user)

@views.route('/mycards', methods=['GET', 'POST'])
@login_required
def mycards():

    return render_template("mycards.html", user=current_user)
