from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    FloatField,
    IntegerField,
    SelectField,
)
from wtforms.validators import DataRequired, Email


class UserForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


class EditMovieForm(FlaskForm):
    movie_name = StringField("Movie Name", validators=[DataRequired()])
    movie_director = StringField("Director", validators=[DataRequired()])
    movie_release_date = IntegerField(
        "Release Date", validators=[DataRequired()]
    )
    movie_rating = FloatField("Rating", validators=[DataRequired()])
    submit = SubmitField("Submit")


class DeleteForm(FlaskForm):
    submit = SubmitField("Delete")


class EditForm(FlaskForm):
    submit = SubmitField("Edit")


class UserMovieForm(FlaskForm):
    submit = SubmitField("User Movies")


class ADDUserMovie(FlaskForm):
    movie_to_add = SelectField(
        "Movie", choices=[], coerce=int, validators=[DataRequired()]
    )
    submit = SubmitField("Add Movie")


class AddMovieForm(FlaskForm):
    movie_name = StringField("Movie Name", validators=[DataRequired()])
    submit = SubmitField("Submit")
