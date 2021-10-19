from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import StringField
from wtforms.fields.simple import PasswordField, SubmitField

class FormRegistro(FlaskForm):
    nombre = StringField()
    usuario = StringField()
    correo = StringField()
    contrasena = PasswordField()
    enviar = SubmitField('Registrarme')

class FormLogin(FlaskForm):
    usuario = StringField()
    contrasena = PasswordField()
    enviar = SubmitField('Iniciar Sesion')