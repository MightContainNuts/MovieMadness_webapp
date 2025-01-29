from flask import Blueprint, render_template, request, g, redirect, url_for
from application.services.forms import (
    UserForm,
    DeleteForm,
    EditForm,
    UserMovieForm,
    ADDUserMovie,
)

user = Blueprint("user", __name__)


@user.route("/users")
def list_users():
    edit_form = EditForm()
    delete_form = DeleteForm()
    user_movie_form = UserMovieForm()
    with g.data_manager as dm:
        users = dm.get_all_users()
    return (
        render_template(
            "users.html",
            users=users,
            delete_form=delete_form,
            edit_form=edit_form,
            user_movie_form=user_movie_form,
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


@user.route("/user/<int:user_id>/movies", methods=["GET"])
def list_user_movies(user_id):
    form = ADDUserMovie()
    with g.data_manager as dm:
        actual_user = dm.get_user_from_id(user_id)
        user_movie_list = dm.get_user_movies(user_id)
        movies = dm.get_all_movies()
        form.movie_to_add.choices = [
            (movie.movie_id, movie.movie_name) for movie in movies
        ]

    return (
        render_template(
            "user_movies.html",
            actual_user=actual_user,
            form=form,
            user_movie_list=user_movie_list,
            movies=movies,
        ),
        200,
    )


@user.route("/user/<int:user_id>/movies/add", methods=["POST"])
def add_user_movie(user_id):
    print(f"Form Data: {request.form}")
    form = ADDUserMovie()
    with g.data_manager as dm:
        movies = dm.get_all_movies()
        form.movie_to_add.choices = [
            (movie.movie_id, movie.movie_name) for movie in movies
        ]

    if form.validate_on_submit():
        movie_id = int(form.movie_to_add.data)  # <-- Now correctly passed
        print(f"Adding movie {movie_id} to user {user_id}")  # Debugging output
        with g.data_manager as dm:
            dm.add_user_movie(user_id, movie_id)
    else:
        print(f"Form did not validate: {form.errors}")

    return redirect(url_for("user.list_user_movies", user_id=user_id))
