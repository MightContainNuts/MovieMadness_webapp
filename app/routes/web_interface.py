from flask import Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return "I am a teapot, short and stout", 200
