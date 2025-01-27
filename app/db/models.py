from sqlalchemy import Integer, String, Float
from app.__init__py import db, create_app


class Users(db.Model):
    __tablename__ = "users"
    user_id = db.Column(Integer, primary_key=True, autoincrement=True)
    username = db.Column(String(50), unique=True)
    email = db.Column(String(50), unique=True)
    first_name = db.Column(String(50))
    last_name = db.Column(String(50))

    def __repr__(self):
        return (
            f"<User(id={self.user_id}',"
            f"username='{self.username}', "
            f"email='{self.email}', "
            f"first_name='{self.first_name}', "
            f"last_name='{self.last_name}')>"
        )

    def __str__(self):
        return f"{self.username}"


class Movies(db.Model):
    __tablename = "movies"
    movie_id = db.Column(Integer, primary_key=True, autoincrement=True)
    movie_name = db.Column(String(50))
    movie_director = db.Column(String(50))
    movie_release_date = db.Column(Integer)
    movie_rating = db.Column(Float)

    def __repr__(self):
        return (
            f"<Movie(id={self.movie_id}',"
            f"name='{self.movie_name}', "
            f"director='{self.movie_director}', "
            f"release_date='{self.movie_release_date}', "
            f"rating='{self.movie_rating}')>"
        )

    def __str__(self):
        return f"{self.movie_name}"


def _create_database_models():
    with app.app_context():
        app.logger.info("Creating database models...")
        db.create_all()
        app.logger.info("Database models created successfully.")


if __name__ == "__main__":
    app = create_app("development")
    with app.app_context():
        print("Creating database models...")
        db.create_all()
        print("Database models created successfully.")
