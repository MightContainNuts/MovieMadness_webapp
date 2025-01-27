from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config
from app.services.logger import setup_logger

from app.routes.web_interface import main


bootstrap = Bootstrap()
db = SQLAlchemy()
logger = setup_logger(__name__)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    bootstrap.init_app(app)
    db.init_app(app)

    # TODO add blueprints here
    app.register_blueprint(main)
    logger.info("App created using '%s' config", config_name)
    return app
