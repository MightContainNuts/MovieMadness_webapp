from flask import Blueprint, render_template, request, g, redirect, url_for
from application.services.forms import MovieForm, DeleteForm, EditForm

movie = Blueprint("movie", __name__)


@movie.route("/movies")
def list_movies():
    delete_form = DeleteForm()
    edit_form = EditForm()
    with g.data_manager as dm:
        movies = dm.get_all_movies()
    return (
        render_template(
            "movies.html",
            movies=movies,
            edit_form=edit_form,
            delete_form=delete_form,
        ),
        200,
    )


@movie.route("/movie/<int:movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    with g.data_manager as dm:
        movie_to_edit = dm.get_movie_from_id(movie_id)
        if not movie_to_edit:
            print(f"Movie with ID {movie_id} not found.")
            return "Movie not found", 404
    form = MovieForm()
    if request.method == "GET":
        form.movie_name.data = movie_to_edit.movie_name
        form.movie_director.data = movie_to_edit.movie_director
        form.movie_release_date.data = movie_to_edit.movie_release_date
        form.movie_rating.data = movie_to_edit.movie_rating

    if form.validate_on_submit():
        with g.data_manager as data_manager:
            data_manager.update_movie(movie_id, form.data)
        return redirect(url_for("main.index"))
    return render_template("movie.html", movie=movie_to_edit, form=form), 200


@movie.route("/movie/<int:movie_id>/delete", methods=["POST"])
def delete_movie(movie_id):
    form = DeleteForm()
    if form.validate_on_submit():
        with g.data_manager as dm:
            dm.delete_movie(movie_id)
    return redirect(url_for("main.index"))


@movie.route("/movie/add", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()
    if form.validate_on_submit():
        with g.data_manager as dm:
            dm.add_movie(form.data)
        redirect(url_for("main.index")), 200
    return render_template("movie.html", form=form), 200
