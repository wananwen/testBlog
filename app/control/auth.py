from flask import Blueprint
from flask import render_template
from flask.ext.login import LoginManager
from ..model.base import User
from flask.ext.login import login_required

loginManager = LoginManager()
loginManager.session_protection = "Stong"
loginManager.login_view = 'auth.login'

bp = Blueprint("auth", __name__)


@bp.route("/login")
def login():
    return render_template("auth/login.html")


@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp.route('/secret')
@login_required
def secret():
    return 'only authenticated users are allowed'
