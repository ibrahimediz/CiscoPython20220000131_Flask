from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,PasswordField, BooleanField
from wtforms.validators import DataRequired,Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')