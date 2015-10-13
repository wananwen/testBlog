import os

basedir = os.path.basedir(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
        "sqlite:///"+os.path.join(basedir, "data_dev.sqlite")


class TestConfig(Config):
    TESTING = True
    SQLCHEMY_DATABASE_UTI = os.environ.get("TEST_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "data_test.sqlite")


class ProductionConfig(Config):
    SQLCHEMY_DATABSE_URI = os.environ.get("DATABASE_URL") or \
    "sqlite:///" + os.path.join(basedir, "data.sqlite")


config = {
    "development" : DevelopmentConfig
    "testing" : TestConfig
    "production" : ProductionConfig
    "default" : DevelopmentConfig

}