from flask import Blueprint, render_template

dist = Blueprint('dist',__name__)

@dist.route("/dist")
def look_out():
    return render_template("dist.html")

@dist.route("/output")
def response():
    return "html aqui"