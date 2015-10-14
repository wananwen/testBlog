from flask.ext.script import Manager
from app import create_app
from app import db
from app.model.base import Role, User
from itertools import chain


db_column = {
    "Role" : Role,
    "User" : User
}

app = create_app("development")
manager = Manager(app)


@manager.command
def create_db():
    db.create_all()


@manager.command
def add_a_column(add_name, column):
    if column != "Role" and column != "User":
        print("column must 'Role'or'User' ")
    else:
        tmp = Role(name=add_name)
        #tmp = db_column[column](add_name)
        db.session.add(tmp)


@manager.command
def delete_db():
    db.drop_all()

@manager.command
def get_config(config):
    print("%s" % (config) )



if __name__ == "__main__":
    manager.run()
