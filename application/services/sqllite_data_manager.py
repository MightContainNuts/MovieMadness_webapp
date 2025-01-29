# Description: all services related to the sql lite operations
from typing import override, Optional

from application.app_factory import db
from application.db.models import User, Movie, UserMovie
from application.services.data_manager import DataManagerInterface
from application.services.logger import setup_logger

logger = setup_logger(__name__)

UserDict = dict[str, str]
MovieDict = dict[str, str]


class SQLiteDataManger(DataManagerInterface):
    def __init__(self):
        self.session = None  # Placeholder for session management

    def __enter__(self):
        """Set up the resource (e.g., database session)."""
        self.session = db.session
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Clean up resources when the context is exited."""
        if self.session:
            self.session.remove()

    def __str__(self):
        return "SQLite Data Manager"

    def __repr__(self):
        return "SQLite Data Manager"

    @override
    def get_all_users(self) -> Optional[list[User]]:
        logger.info("Getting get_all_users")
        try:
            users = db.session.query(User).all()
            logger.info(f"Users: {users}")
            return users
        except Exception as e:
            logger.error(f"Error getting all users: {e}")
            return None

    @override
    def add_user(self, new_user: UserDict) -> None:
        try:
            self.session.add(
                User(
                    username=new_user["username"],
                    email=new_user["email"],
                    first_name=new_user["first_name"],
                    last_name=new_user["last_name"],
                )
            )
            self.session.commit()
            logger.info("User added successfully")
        except Exception as e:
            logger.error(f"Error adding user: {e}")
            self.session.rollback()

    @override
    def delete_user(self, user_id) -> None:
        """delete user from database"""
        logger.info("Deleting user %s", user_id)
        try:
            user = self.get_user_from_id(user_id)
            self.session.delete(user)
            self.session.commit()
            logger.info("User deleted successfully %s", id)
        except Exception as e:
            logger.error(f"Error deleting user: {e}")
            self.session.rollback()

    @override
    def update_user(self, user_id: int, new_user: UserDict) -> None:
        """modify user in database"""
        logger.info("Modifying user %s", user_id)
        try:
            user = self.get_user_from_id(user_id)
            user.username = new_user["username"]
            user.email = new_user["email"]
            user.first_name = new_user["first_name"]
            user.last_name = new_user["last_name"]
            self.session.commit()
            logger.info("User modified successfully %s", user_id)
        except Exception as e:
            logger.error(f"Error modifying user: {e}")
            self.session.rollback()

    @override
    def get_all_movies(self) -> Optional[list[Movie]]:
        """get all movies from database"""
        try:
            return self.session.query(Movie).all()
        except Exception as e:
            logger.error(f"Error getting all movies: {e}")
            return None

    @override
    def add_movie(self, new_movie: MovieDict) -> None:
        """add movie to db"""
        try:
            self.session.add(
                Movie(
                    movie_name=new_movie["movie_name"],
                    movie_director=new_movie["movie_director"],
                    movie_release_date=new_movie["movie_release_date"],
                    movie_rating=new_movie["movie_rating"],
                )
            )
            self.session.commit()
            logger.info("Movie added successfully")
        except Exception as e:
            logger.error(f"Error adding movie: {e}")
            self.session.rollback()

    @override
    def update_movie(self, movie_id, updated_movie):
        movie = self.get_movie_from_id(movie_id)
        if movie:
            movie.movie_name = updated_movie["movie_name"]
            movie.movie_director = updated_movie["movie_director"]
            movie.movie_release_date = updated_movie["movie_release_date"]
            movie.movie_rating = updated_movie["movie_rating"]
            self.session.commit()
            logger.info(f"Movie with id {movie_id} updated successfully")
        else:
            logger.info("Movie not found")

    @override
    def delete_movie(self, movie_id):
        """delete movie from database"""
        movie = self.get_movie_from_id(movie_id)
        if movie:
            self.session.delete(movie)
            self.session.commit()
            logger.info(f"Movie with id {movie_id} deleted successfully")
        else:
            logger.info("Movie not found")

    # private Helper methods

    def get_movie_from_id(self, movie_id):
        """get movie from database"""
        movie = (
            self.session.query(Movie)
            .filter(Movie.movie_id == movie_id)
            .first()
        )
        return movie

    def get_user_from_id(self, user_id):
        """get movie from database"""
        user = self.session.query(User).filter(User.user_id == user_id).first()
        return user

    def get_user_movies(self, user_id):
        """get user movies from database"""
        user = self.get_user_from_id(user_id)

        return user.movies

    def add_user_movie(self, user_id, movie_id):
        """add user movie to database"""
        new_user_movie = UserMovie(user_id=user_id, movie_id=movie_id)
        self.session.add(new_user_movie)
        self.session.commit()
        logger.info(
            f"Movie with id {movie_id} added to user with id {user_id}"
        )
