from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    nombre = StringField('Nombre Equipo', validators=[InputRequired('Nombre de equipo requerido')])
    passw = PasswordField('Contraseña', validators=[InputRequired('Contraseña requerida')])


class SignupForm(FlaskForm):

    nombre = StringField('Nombre Equipo', validators=[InputRequired('Nombre de equipo requerido')])
    passw = PasswordField('Contraseña', validators=[InputRequired('Contraseña requerida')])
    submit = SubmitField("Create equipo")
