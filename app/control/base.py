
from flask import Blueprint
from flask import render_template
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask import session, redirect, url_for, flash


base_bp = Blueprint("base", __name__)


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@base_bp.route("/base", methods=['GET', 'POST'])
def base():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('/base'))
    return render_template('base.html', form=form, name=session.get('name'))
