import requests
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from .import bp as auth 
from flask_login import current_user, logout_user, login_user, login_required




@auth.route('/cart', methods=['GET','POST'])
@login_required
def cart():
    return render_template("cart.html.j2")