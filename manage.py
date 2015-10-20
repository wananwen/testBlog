from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app import create_app
from app.model.base import db, Role, User

app = create_app("development")
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def create_db():
    db.create_all()


@manager.command
def add_role(name):
    role = Role(name=name)
    db.session.add(role)
    db.session.commit()
    print(role.id)


@manager.command
def add_user(email):
    user = User(email=email, username="LiMing",
                passwd="cat")
    db.session.add(user)
    db.session.commit()
    print(user.userId)


@manager.command
def query_user(email):
    user = User.query.filter_by(email=email).first()
    print(user)


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
