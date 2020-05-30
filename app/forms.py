from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Введите имя:', validators=[DataRequired()])
    password = PasswordField('Введите пароль:', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class RegistrationForm(FlaskForm):
    username = StringField('Введите имя:', validators=[DataRequired()])
    email = StringField('Введите email:', validators=[DataRequired(), Email()])
    password = PasswordField('Введите пароль:', validators=[DataRequired()])
    password2 = PasswordField(
        'Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Регистрация')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField('Ваше имя:', validators=[DataRequired()])
    about_me = TextAreaField('Информация о вас:', validators=[Length(min=0, max=140)])
    submit = SubmitField('Опубликовать')

class PostForm(FlaskForm):
    post = TextAreaField('Добро пожаловать на мой первый сайт! Ты можешь здесь написать какой-то текст:', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Опубликовать')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')

