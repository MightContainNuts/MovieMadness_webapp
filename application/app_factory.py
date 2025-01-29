from flask import Flask, g
from flask_bootstrap import Bootstrap
from config import config
from application.services.logger import setup_logger
from application.db.db import db


logger = setup_logger(__name__)


def create_app(config_name):
    logger.info("Creating app using '%s' config", config_name)

    # Initialize the Flask app
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize the app extensions
    bootstrap = Bootstrap()
    bootstrap.init_app(app)

    db.init_app(app)

    # Add before request function
    @app.before_request
    def before_request():
        from application.services.sqllite_data_manager import SQLiteDataManger

        g.data_manager = SQLiteDataManger()

    # Register blueprints
    from application.routes.user_routes import user
    from application.routes.main_routes import main
    from application.routes.errors import errors
    from application.routes.movie_routes import movie

    app.register_blueprint(user, url_prefix="/")
    app.register_blueprint(errors, url_prefix="/")
    app.register_blueprint(main, url_prefix="/")
    app.register_blueprint(movie, url_prefix="/")

    logger.info("App created using '%s' config", config_name)

    return app
