from flask import Blueprint, render_template, request
from business import Business

dist = Blueprint('dist',__name__)

@dist.route("/", methods=["GET"])
def look_out():
    return render_template("dist.html")

@dist.route("/", methods=["POST"])
def look_out_post():
    address=request.form["ad"]

    b = Business()
    dist = b.process_request(address)

    if type(dist)==str:
        return "No results"

    print(address)
    return render_template("output.html", len=len(dist), addressform=dist)
