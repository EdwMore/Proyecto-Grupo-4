import os
from flask import Flask, render_template, request
from flask.helpers import url_for
from flask_wtf import form
from werkzeug.utils import redirect
from forms import FormLogin, FormRegistro

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def inicio():
    return render_template('Header.html')

@app.route('/registro/', methods=["GET", "POST"])
def registro():
    if request.method == "GET":
        formulario = FormRegistro()
        return render_template('Registro.html', form=formulario)
    else:
        formulario = FormRegistro(request.form)
        if formulario.validate_on_submit():
            return render_template('Registro.html', form=formulario)

@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        formulario = FormLogin()
        return render_template('InicioSesion.html', form=formulario)
    else:
        formulario = FormLogin(request.form)
        if formulario.validate_on_submit:
            return render_template('InicioSesion.html', form=formulario)
    
    