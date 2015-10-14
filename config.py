import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or \
        "this is my own blog"
        
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
        "sqlite:///"+os.path.join(basedir, "data_dev.sqlite")


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "data_test.sqlite")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
    "sqlite:///" + os.path.join(basedir, "data.sqlite")


config = {
    "development" : DevelopmentConfig,
    "testing" : TestConfig,
    "production" : ProductionConfig,
    "default" : DevelopmentConfig

}