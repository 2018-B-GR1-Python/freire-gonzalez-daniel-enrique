# flask.py
# set FLASK_APP=flask.py flask run
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"
