import os
from pathlib import Path

base_dir = Path(__file__).resolve().parent
db_path_dev = base_dir / "app" / "data" / "moviemadness.sqlite"
db_path_test = base_dir / "app" / "data" / "test_library.sqlite"
db_path_prod = base_dir / "app" / "data" / "moviemadness.sqlite"


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or "hard to guess string"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    HOST = "0.0.0.0"  # Default host
    PORT = 5000


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path_dev}"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path_test}"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path_prod}"


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
