from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, TextAreaField, SubmitField, EmailField, RadioField, SelectField, \
    FileField, PasswordField
from wtforms.validators import DataRequired


# title
# surname
# name
# education
# profession
# sex
# motivation
# ready
class RegisterForm(FlaskForm):
    email = StringField('login/email', validators=[DataRequired()])
    fpassword = PasswordField('Password', validators=[DataRequired()])
    spassword = PasswordField('Repeat password', validators=[DataRequired()])

    surname = StringField('surname', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    age = StringField('age', validators=[DataRequired()])
    position = StringField('position', validators=[DataRequired()])
    speciality = StringField('speciality', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    submit = SubmitField('Доступ')


class LoadForm(FlaskForm):
    fileName = FileField()


class TwoLogin(FlaskForm):
    fid = StringField('id астронафта', validators=[DataRequired()])
    fpassword = PasswordField('Пароль астронафта', validators=[DataRequired()])
    sid = StringField('id капитана', validators=[DataRequired()])
    spassword = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')

