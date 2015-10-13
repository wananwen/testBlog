import os
from flask.ext.script import Manager
from . import create_app
from . import db
from model import Role, User
from itertools import chain


role_tmp = ['King', 'Teacher', 'Killer']
user_tmp = ['LiLei', 'HanMeiMei', 'LiLi']
role_add_to_db = []
user_add_to_db = []


@manager.command
def create_db():
    db.cteare_all()


@manager.command
def add_a_column():
    role_add_to_db.append = Role(role_tmp.pop)
    user_add_to_db.append = User(user_tmp.pop, role_id=role_add_to_db[-1])


@manager.command
def add_to_db():
    tmp = role_add_to_db
    db.session.add_all(chain(role_add_to_db, user_add_to_db))

if __name__ == "__main__":
    app = create_app("development")
    mananer = Manager(app)

    