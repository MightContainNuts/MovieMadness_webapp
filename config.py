import os
from pathlib import Path

base_dir = Path(__file__).resolve().parent
db_path_dev = base_dir / "application" / "db" / "moviemadness.sqlite"
db_path_test = base_dir / "application" / "db" / "test_movie_db.sqlite"
db_path_prod = base_dir / "application" / "db" / "moviemadness.sqlite"

# Convert Path objects to strings
db_path_dev_str = str(db_path_dev)
db_path_test_str = str(db_path_test)
db_path_prod_str = str(db_path_prod)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or "hard to guess string"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    HOST = "0.0.0.0"  # Default host
    PORT = 5000


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path_dev_str}"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path_test_str}"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path_prod_str}"


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
