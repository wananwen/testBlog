from config import config
from flask import Flask
from SQLAlchemy import SqlAlchemy


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    return app


if __name__ = "__main__":
    create_app("development")
    