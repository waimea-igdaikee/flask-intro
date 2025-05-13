from flask import Flask
from flask import render_template
from random import randint

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

@app.get("/random/")
def random():
    random_number = randint(1,100)
    return render_template("pages/random.jinja", number=random_number)

@app.errorhandler(404)
def error404(null):
    return render_template("pages/error404.jinja")