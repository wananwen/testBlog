from flask import Blueprint
from flask import render_template, redirect, url_for, flash, request
from flask.ext.login import login_user, LoginManager, logout_user
from flask.ext.login import login_required
from ..forms import login_forms
from ..model.base import User

loginManager = LoginManager()
loginManager.session_protection = "Stong"
loginManager.login_view = 'auth.login'

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    form = login_forms.loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verity_passwd(form.password.data):
            login_user(user, form.remerber_me.data)
            return redirect(request.arg.get('next') or url_for('base.base'))
        flash("invalid username or password")
    return render_template("auth/login.html", form=form)


@auth_bp.route("/logOut", methods=["POST", "GET"])
@login_required
def loginOut():
    logout_user()
    flash("you have been logout")
    return redirect(url_for("base.base"))


@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth_bp.route('/secret')
@login_required
def secret():
    return 'only authenticated users are allowed'
