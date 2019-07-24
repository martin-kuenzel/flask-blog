from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from flask_blog.models import User

class RegistrationForm(FlaskForm):
    username = StringField( 'Username', validators = [ DataRequired(), Length(min=5,max=20) ] )
    email = StringField('Email', validators = [ DataRequired(), Email() ] )

    password = PasswordField( 'Password', validators = [ DataRequired(), Length(min=5) ] )
    confirm_password = PasswordField( 'Confirm Password', validators = [ DataRequired(), Length(min=5), EqualTo('password') ] )

    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user is None:
            raise ValidationError('Username is already taken')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user is None:
            raise ValidationError('Email already exists')

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [ DataRequired(), Email() ] )
    password = PasswordField( 'Password', validators = [ DataRequired(), Length(min=5) ] )

    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
