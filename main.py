from flask import Flask
from distance import dist

app = Flask(__name__)
app.register_blueprint(dist)

if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)