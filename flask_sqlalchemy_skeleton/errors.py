from flask_sqlalchemy_skeleton import app
from flask import render_template

@app.errorhandler(404)
def not_found():
    return render_template("404.html")


@app.errorhandler(500)
def not_found():
    return render_template("500.html")
    