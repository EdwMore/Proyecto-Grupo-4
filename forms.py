from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import StringField
from wtforms.fields.simple import PasswordField, SubmitField

class FormRegistro(FlaskForm):
    nombre = StringField(validators=[validators.required(), validators.length(min=20)])
    usuario = StringField(validators=[validators.required(), validators.length(min=15, max=50)])
    contrasena = PasswordField(validators=[validators.required(), validators.length(min=10)])
    enviar = SubmitField('Registrarme')

class FormLogin(FlaskForm):
    usuario = StringField(validators=[validators.required()])
    contrasena = PasswordField(validators=[validators.required()])
    enviar = SubmitField('Iniciar Sesion')