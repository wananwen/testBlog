from flask.ext.script import Manager
from app import create_app
from app import db
from app.model.base import Role, User

app = create_app("development")
manager = Manager(app)


@manager.command
def run():
    app.run()


@manager.command
def create_db():
    db.create_all()


@manager.command
def add_a_column(add_name, column):
    tmp = None
    if column == "Role":
        tmp = Role(name=add_name)
    elif column == "User":
        tmp = User(username=add_name)
    else:
        print("the second param must 'Role' or 'User'")
    if tmp is not None:
        db.session.add(tmp)
        db.session.commit()
        print("id = %s" % (tmp.id))


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
