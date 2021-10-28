from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import StringField
from wtforms.fields.simple import PasswordField, SubmitField, TextAreaField

class FormRegistro(FlaskForm):
    nombre = StringField(validators=[validators.required()])
    usuario = StringField(validators=[validators.required(), validators.length(min=4, max=16)])
    correo = StringField(validators=[validators.required()])
    contrasena = PasswordField(validators=[validators.required(), validators.length(min=4, max=16)])
    enviar = SubmitField('Registrarme')

class FormLogin(FlaskForm):
    usuario = StringField(validators=[validators.required()])
    contrasena = PasswordField(validators=[validators.required()])
    enviar = SubmitField('Iniciar Sesion')

class FormCrearJugo(FlaskForm): 
    nombre = StringField()
    descripcion = TextAreaField()
    enviar = SubmitField()