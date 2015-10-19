from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Length, Email


class loginForm(Form):
    email = StringField('Email', validators=[Required(),
                        Length(1, 64), Email()])
    password = PasswordField("Password", validators=[Required()])
    remerber_me = BooleanField("Keep me logged in")
    submit = SubmitField("Login in")
