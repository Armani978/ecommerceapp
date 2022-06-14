from flask import render_template, request, flash, redirect, url_for
import requests
from .import bp as main
from ...forms import Login, Register
from ...models import User
from flask_login import current_user, logout_user, login_user, login_required

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html.j2')

@main.route('/login', methods=['GET','POST'])
def login():
    form = Login()

    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data
        user_query=User.query.filter_by(email=email).first()
        if user_query and user_query.check_hash(password):
            login_user(user_query)
            flash('Welcome','success')
            return redirect(url_for('main.index'))
        return render_template('login.html.j2', form=form)
    return render_template('login.html.j2', form=form)

@main.route('/register', methods=['GET','POST'])
def register():
    form = Register()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            user_dict={
                "first_name" : form.first_name.data.title(),
                "last_name" : form.last_name.data.title(),
                "email": form.email.data.lower(), 
                "password": form.password.data
            }     
            user_object = User()
            user_object.my_dict(user_dict)
            user_object.save()


        
        except:
            flash("Error, try again.", "danger")
            return render_template('register.html.j2', form=form)
        flash("Success! You have registered!")    
        return redirect(url_for('main.login'))
    return render_template('register.html.j2', form=form)

@main.route('/af1', methods=['GET'])
def nike_air_force_one():
    return render_template('af1.html.j2')

@main.route('/jordan4retro', methods=['GET'])
def jordan_4_retro():
    return render_template('j4.html.j2')

@main.route('/dunk', methods=['GET'])
def dunk():
    return render_template('dunk.html.j2')

@main.route('/chromeheartstee', methods=['GET'])
def chromeheartstee():
    return render_template('chrome.html.j2')

@main.route('/palmangels', methods=['GET'])
def palmangels():
    return render_template('palm.html.j2')

@main.route('/navxvlone', methods=['GET'])
def navxvlone():
    return render_template('vlone.html.j2')
@main.route('/cart', methods=['GET','POST'])
@login_required
def cart():
    return render_template("cart.html.j2")