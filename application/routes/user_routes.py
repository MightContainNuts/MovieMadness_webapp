from flask import Blueprint, render_template, request, g, redirect, url_for
from application.services.forms import UserForm, DeleteForm, EditForm

user = Blueprint("user", __name__)


@user.route("/users")
def list_users():
    edit_form = EditForm()
    delete_form = DeleteForm()
    with g.data_manager as dm:
        users = dm.get_all_users()
    return (
        render_template(
            "users.html",
            users=users,
            delete_form=delete_form,
            edit_form=edit_form,
        ),
        200,
    )


@user.route("/user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    with g.data_manager as dm:
        user_to_edit = dm.get_user_from_id(user_id)
        if not user_to_edit:
            print(f"User with ID {user_id} not found.")
            return "User not found", 404
    form = UserForm()
    if request.method == "GET":
        form.username.data = user_to_edit.username
        form.email.data = user_to_edit.email
        form.first_name.data = user_to_edit.first_name
        form.last_name.data = user_to_edit.last_name

    if form.validate_on_submit():
        with g.data_manager as data_manager:
            data_manager.update_user(user_id, form.data)
        return redirect(url_for("main.index"))
    return render_template("user.html", user=user_to_edit, form=form), 200


@user.route("/user/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    form = DeleteForm()
    if form.validate_on_submit():
        with g.data_manager as dm:
            dm.delete_user(user_id)
    return render_template("index.html"), 200


@user.route("/user/add", methods=["GET", "POST"])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        with g.data_manager as dm:
            dm.add_user(form.data)
        return render_template("index.html"), 200
    return render_template("user.html", form=form), 200
