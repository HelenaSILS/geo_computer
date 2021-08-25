from flask import Blueprint, render_template, request
from business import Business

dist = Blueprint('dist',__name__)

@dist.route("/", methods=["GET"])
def look_out():
    """
    calls the home page to be rendered
    :return: dist.html
    """
    return render_template("dist.html")

@dist.route("/", methods=["POST"])
def look_out_post():
    """
    calls the requests data after the POST method is sent. If everything is ok, it returns an HTML page,
    otherwise it return an string.
    :return: output.html
    """
    address=request.form["ad"]
    b = Business()
    dist = b.process_request(address)

    if type(dist)==str:
        return "No results"

    print(address)
    return render_template("output.html", len=len(dist), addressform=dist)
