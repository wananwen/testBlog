from flask.ext.script import Manager
from app import create_app
from app.model.base import db, Role, User

app = create_app("development")
manager = Manager(app)


@manager.command
def run():
    app.run()


@manager.command
def create_db():
    db.create_all()


@manager.command
def add_a_column(add_name, column, email="gudengguzhou@163.com", passwd="cat"):
    tmp = None
    if column == "Role":
        tmp = Role(name=add_name)
    elif column == "User":
        tmp = User(username=add_name)
        print(tmp.userId)
    else:
        print("the second param must 'Role' or 'User'")
    if tmp is not None:
        db.session.add(tmp)
        db.session.commit()


@manager.command
def delete_db():
    db.drop_all()


@manager.command
def query_db(column):
    if column == "Role":
        print(Role.query.all())
    elif column == "User":
        print(User.query.all())
    else:
        print("column must 'Role'or 'User'")


if __name__ == "__main__":
    manager.run()
