from flask import Flask, jsonify, render_template
from business import Business
from distance import dist

app = Flask(__name__)
app.register_blueprint(dist)

@app.route('/')
def hello_world():
    return "hello"



if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)