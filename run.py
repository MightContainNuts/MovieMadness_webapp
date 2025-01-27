# Description: This file is used to run the application
from application.app_factory import create_app
from application.services.logger import setup_logger
from application.db.db import db

app = create_app("development")

logger = setup_logger(__name__)


def _create_database_models():
    with app.app_context():  # Ensure app context is active
        try:
            print("Creating database models")
            logger.info("Creating database models")
            db.create_all()  # This creates the database models (tables)
            logger.info("Database models created successfully")
            print("Database models created successfully")
        except Exception as e:
            logger.error(f"Error creating database models: {e}")
            print(f"Error creating database models: {e}")


if __name__ == "__main__":
    app.run()
