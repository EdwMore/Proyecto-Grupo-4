from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import StringField
from wtforms.fields.simple import PasswordField, SubmitField

class FormRegistro(FlaskForm):
    nombre = StringField(validators=[validators.required()])
    usuario = StringField(validators=[validators.required()])
    correo = StringField(validators=[validators.required()])
    contrasena = PasswordField(validators=[validators.required()])
    enviar = SubmitField('Registrarme')

class FormLogin(FlaskForm):
    usuario = StringField(validators=[validators.required()])
    contrasena = PasswordField(validators=[validators.required()])
    enviar = SubmitField('Iniciar Sesion')