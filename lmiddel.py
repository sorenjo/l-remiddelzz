from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from data import Opgave
import csv
import os

app = Flask(__name__)

def gen_opg():
    task = Opgave()
    return render_template(index.htmltemplate, task = task)


@app.route("/")
@app.route("/index")
@app.route("/index.html")
def index():
    return render_template("index.htmltemplate")

@app.route("/opgave/<opgnr>")
def opgave(opgnr):
    
