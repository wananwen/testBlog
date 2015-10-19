
from flask import Blueprint
from flask import render_template
from flask import session, redirect, url_for
from ..forms.base_forms import NameForm
from ..model.base import db, User


base_bp = Blueprint("base", __name__)


@base_bp.route("/", methods=['GET', 'POST'])
def base():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['know'] = False
        else:
            session['know'] = True
        session['name'] = user
        return redirect(url_for('.base'))
    return render_template('index.html', form=form, name=session.get('name'))
