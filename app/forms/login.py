from flask.ext.wtf import Form
from  wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import Required, Length, email


class loginForm(Form):
    email = StringField('Email', validators=[Required(), \
                                    Length(1, 64), email()])
    password = PasswordField("Password", validators=[Required])
    remerber_me = BooleanField("Keep me logged in")
    submit = SubmitField("Submit")

