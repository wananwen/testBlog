from config import config
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app.control import base
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

moment = Moment()
bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    app.register_blueprint(base.bp)
    return app
