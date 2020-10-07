from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from data import Opgave
import csv
import os

app = Flask(__name__)
app.secret_key = "1337"

@app.route("/")
@app.route("/index")
@app.route("/index.html")
def index():
    return render_template("index.htmltemplate")

@app.route("/opgave/")
def opgave():
    return render_template("index.htmltemplate", opg = Opgave())

@app.route("/rigtigt/")
def rigtigt():
    return render_template("svar.htmltemplate", rigtigt = True)

@app.route("/forkert/")
def forkert():
    return render_template("svar.htmltemplate", rigtigt = False)

if __name__ == "__main__":
    with app.app_context():
        pass
    app.run(debug=True)
