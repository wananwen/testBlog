from config import config
from flask import Flask
from app.control import base
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from app.model.base import db
from app.control import auth


moment = Moment()
bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    bootstrap.init_app(app)
    db.init_app(app)
    auth.loginManager.init_app(app)
    moment.init_app(app)
    register_app(app)
    return app


def register_app(app):
    app.register_blueprint(base.base_bp)
    app.register_blueprint(auth.auth_bp, url_prefix="/auth")
