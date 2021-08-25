from flask import Flask, jsonify, render_template
from business import Business
from distance import dist

app = Flask(__name__)
app.register_blueprint(dist)

@app.route('/')
def hello_world():
    #b = Business()
    #if (b.isvalid("Sultanahmet Camii İç Yolları")):
    #    dist = b.sendyandex("Sultanahmet Camii İç Yolları")
    #    print(dist)

    return 'Hello World'



if __name__ == '__main__':
    b = Business()
    if (b.isvalid("Sultanahmet Camii İç Yolları")):
        dist = b.sendyandex("Sultanahmet Camii İç Yolları")
        print(dist)
    app.run(debug=True, port=5000, threaded=True)