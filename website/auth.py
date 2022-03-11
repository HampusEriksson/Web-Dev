from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Card, User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, currency = 100, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

@login_required
@auth.route('/admin', methods=['GET', 'POST'])
def admin():
    if current_user.id != 1:
        flash('Only admins can add cards', category='error')
    if request.method == 'POST':
        print(request.form.get('name'))
        name = request.form.get('name')
        rarity = request.form.get('rarity')
        price = request.form.get('rarity')
        file = request.files['file']
        

        user = Card.query.filter_by(name=name).first()
        if current_user.id != 1:
            flash('Only admins can add cards', category='error')
        elif user:
            flash('Card already exists.', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 1 character.', category='error')
        else:
            
            new_card = Card(name=name, rarity=rarity,user_id=current_user.id, price = price, filename=file.filename)
            db.session.add(new_card)
            db.session.commit()
            flash('Card created!', category='success')

    return render_template("admin.html", user=current_user, cards = Card.query.all())
