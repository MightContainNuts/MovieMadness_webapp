from flask import Blueprint, render_template


main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html"), 200


@main.route("/users")
def list_users():
    pass
    return "List of users", 200
