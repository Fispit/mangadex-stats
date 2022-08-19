from flask import Flask,jsonify,render_template
import requests


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/demographics")
def demographics():
    return render_template("demographics.html")

@app.route("/routes")
def routespage():
    return render_template("routes.html")

@app.route("/s_map")
def smappage():
    return render_template("s_map.html")

@app.route("/usage")
def usagepage():
    return render_template("usage.html")
