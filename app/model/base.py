from . import db


class User(db.model):
    __tablename__ = "User"
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey("Roles.id"))

    def __reqr__(self):
        return "user name %s" % (self.username)


class Role(db.model):
    __tablename__ = "Roles"
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    users = db.relationship("User", backref="role")

    def __reqr__(self):
        return "Role's name is %s" % (self.name)
