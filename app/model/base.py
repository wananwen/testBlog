from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from ..control.auth import loginManager

db = SQLAlchemy()




class User(UserMixin, db.Model):
    __tablename__ = "User"
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey("Roles.id"))
    passwd_hash = db.Column(db.String(128))
    email = db.Column(db.Integer, primary_key=True)

    @property
    def passwd(self):
        raise AttributeError('passwd is not a readable attribute')

    @passwd.setter
    def passwd(self, password):
        self.passwd_hash = generate_password_hash(password)

    def verity_passwd(self, password):
        return check_password_hash(self.passwd_hash, password)

    def __reqr__(self):
        return "user name %s" % (self.username)


class Role(db.Model):
    __tablename__ = "Roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    users = db.relationship("User", backref="role")

    def __reqr__(self):
        return "Role's name is %s" % (self.name)
