from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("pages/home.jinja")


@app.get("/test/")
def test():
    return render_template("pages/test.jinja")

@app.get("/about/")
def about():
    return render_template("pages/about.jinja")