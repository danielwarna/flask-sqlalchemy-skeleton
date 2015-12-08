from flask_sqlalchemy_skeleton import app, db

from flask import render_template, flash, request, redirect, url_for
from models import *

from flask.ext.login import login_user, login_required, logout_user, current_user

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/login/')
def login():
    
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":

        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email, password=password).first()

        if user:
            login_user(user)
            flask.flash("Login successfull")

            return redirect(url_for('index'))

        else:
            flash("Login failed")
            return redirect(url_for("login"))



@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))