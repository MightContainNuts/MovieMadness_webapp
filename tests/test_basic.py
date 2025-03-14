from application.app_factory import create_app
import pytest


@pytest.fixture
def client():
    """Fixture to provide a test client."""
    app = create_app("testing")
    with app.test_client() as client:  # Ensure to use the test client
        yield client


def test_app_running(client):
    response = client.get("/")
    assert response.status_code == 200


def test_non_existent_route(client):
    """Test a non-existent route."""
    response = client.get("/nonexistent")
    assert response.status_code == 404


def test_method_not_allowed(client):
    """Test method not allowed on a route."""
    response = client.post("/")
    assert response.status_code == 405


def test_list_movies(client):
    response = client.get("/movies")
    assert response.status_code == 200


def test_list_users(client):
    response = client.get("/users")
    assert response.status_code == 200


def test_add_movie(client):
    response = client.get("/movie/add")
    assert response.status_code == 200


def test_add_user(client):
    response = client.get("/user/add")
    assert response.status_code == 200


def test_delete_movie(client):
    response = client.post("/movie/1/delete")
    assert response.status_code == 302


def test_delete_user(client):
    response = client.post("/user/1/delete")
    assert response.status_code == 200
