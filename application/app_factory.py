from flask import Flask
from flask_bootstrap import Bootstrap
from config import config
from application.services.logger import setup_logger
from application.db.db import db


from application.routes.web_interface import main
from application.routes.errors import errors


bootstrap = Bootstrap()
logger = setup_logger(__name__)


def create_app(config_name):
    logger.info("Creating app using '%s' config", config_name)
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    bootstrap.init_app(app)
    db.init_app(app)

    # TODO add blueprints here
    app.register_blueprint(main)
    app.register_blueprint(errors)
    logger.info("App created using '%s' config", config_name)

    return app
