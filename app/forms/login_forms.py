from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Length, Email, EqualTo


class loginForm(Form):
    email = StringField('Email', validators=[Required(),
                        Length(1, 64), Email()])
    password = PasswordField("Password", validators=[Required()])
    remerber_me = BooleanField("Keep me logged in")
    submit = SubmitField("Login in")


class registerForm(Form):
    email = StringField("Email", validators=[Required(),
                        Length(1, 64), Email()])
    username = StringField("Username", validators=[Required(), Length(1, 64)])

    passwd = PasswordField("Password", validators=[Required(),
                           EqualTo('passwd2', ' passwords must be march')])
    passwd2 = PasswordField("Comfirm password", validators=[Required()])
    submit = SubmitField("Register")
