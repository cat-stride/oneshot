from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    mail = StringField('mail', validators=[Required(), Length(1, 64),
                        Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    mail = StringField('mail', validators=[Required(), Length(1, 64),
                        Email()])
    username = StringField('Username', validators=[Required(), Length(1, 64), 
                                                    Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                        'Usernames must have only letters, '
                                                        'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', 
                                                    message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    wechat_id = StringField('Wechat Id', validators=[Required()])
    submit = SubmitField('Sign In')

    def validate_email(self, field):
        if User.query.filter_by(mail=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already taken.')

    def validate_wechatid(self, field):
        if User.query.filter_by(wechat_id=field.data).first():
            raise ValidationError('Wechat id already taken.')
