from config import config
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app.control.base import base_bp
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

moment = Moment()
bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_blueprint(base_bp)
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    return app
