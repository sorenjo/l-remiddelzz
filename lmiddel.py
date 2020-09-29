from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from data import Data
import csv
import os

app = Flask(__name__)

def gen_opg():
    Data()


@app.route("/")
@app.route("/index")
@app.route("/index.html")
def index():
    return render_template("index.htmltemplate")

@app.route("/opgave/<opgnr>")
def opgave(opgnr):
    
