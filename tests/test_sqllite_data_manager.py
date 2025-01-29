import pytest
from application.app_factory import create_app
from application.services.sqllite_data_manager import SQLiteDataManger


@pytest.fixture
def app():
    """Fixture to provide a Flask app instance."""
    app = create_app("testing")
    yield app


@pytest.fixture
def data_manager(app):
    """Fixture to provide an instance of the data manager
    with application context."""
    with app.app_context():
        with SQLiteDataManger() as data_manager:
            yield data_manager


def test_session_initialization(data_manager):
    assert data_manager.session is not None, "Session should be initialized"


def test_get_all_users(app, data_manager):
    users = data_manager.get_all_users()
    assert users is not None
    assert len(users) == 0


def test_add_user(app, data_manager):
    new_user = {
        "username": "test_user2",
        "email": "test2@test.com",
        "first_name": "Foo",
        "last_name": "Bar",
    }
    data_manager.add_user(new_user)
    users = data_manager.get_all_users()
    assert len(users) == 1


def test_modify_user(app, data_manager):
    modify_user = {
        "username": "modified_user",
        "email": "test2@test.com",
        "first_name": "Modify",
        "last_name": "User",
    }

    IDX = 1
    data_manager.update_user(IDX, modify_user)
    assert len(data_manager.get_all_users()) == 1
    assert data_manager.get_all_users()[0].username == "modified_user"


def test_delete_user(app, data_manager):
    users = data_manager.get_all_users()
    assert len(users) == 1
    data_manager.delete_user(1)
    users = data_manager.get_all_users()
    assert len(users) == 0


def test_get_all_movies(app, data_manager):
    movies = data_manager.get_all_movies()
    assert movies is not None
    assert len(movies) == 0


def test_add_movie(app, data_manager):
    new_movie = {
        "movie_name": "test_movie",
        "movie_director": "test_director",
        "movie_release_date": 2021,
        "movie_rating": 5.0,
    }
    data_manager.add_movie(new_movie)
    movies = data_manager.get_all_movies()
    assert len(movies) == 1
    assert movies[0].movie_name == "test_movie"


def test_update_movie(app, data_manager):
    update_movie = {
        "movie_name": "updated_movie",
        "movie_director": "updated_director",
        "movie_release_date": 2025,
        "movie_rating": 9.9,
    }
    IDX = 1
    data_manager.update_movie(IDX, update_movie)
    movies = data_manager.get_all_movies()
    assert len(movies) == 1
    assert movies[0].movie_name == "updated_movie"


def test_delete_movie(app, data_manager):
    movies = data_manager.get_all_movies()
    assert len(movies) == 1
    data_manager.delete_movie(movie_id=1)
    movies = data_manager.get_all_movies()
    assert len(movies) == 0
