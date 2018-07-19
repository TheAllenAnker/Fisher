# Author: Allen Anker
# Created by Allen Anker on 18/07/2018
from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, DataRequired, Email, ValidationError
from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='Email format does not correct')])

    password = PasswordField(validators=[DataRequired(message='Password cannot be empty'),
                                         Length(6, 32)])

    nickname = StringField(validators=[DataRequired(),
                                       Length(2, 10, message='Nickname length must be 2 to 10 characters')])

    def validate_email(self, field):
        """
        Search if the email has already existed
        :return:
        """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is registered.')

    def validate_nickname(self, field):
        """
        Search if the nickname has already existed
        :return:
        """
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('Nickname cannot be used.')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='Email format does not correct')])

    password = PasswordField(validators=[DataRequired(message='Password cannot be empty'),
                                         Length(6, 32)])

