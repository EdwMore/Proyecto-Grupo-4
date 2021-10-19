import os
import functools

from flask import Flask, render_template, request, url_for, g, session
from werkzeug.utils import redirect
from forms import FormLogin, FormRegistro
from models import usuario

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

def loginRequerido(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login'))
        
        return view(**kwargs)
    
    return wrapped_view

@app.before_request
def UsuarioAutentico():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else: 
        g.user = usuario.cargar(user_id)


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
        if formulario.validate_on_submit:
            print("me valido")
            ob_usuario = usuario(formulario.nombre.data, formulario.usuario.data, formulario.correo.data, formulario.contrasena.data)
            if ob_usuario.insertar():
                return render_template('Registro.html', exito="Se ha registrado su cuenta.")
            
        return render_template('Registro.html', form=formulario, mensaje="")

@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        formulario = FormLogin()
        return render_template('InicioSesion.html', form=formulario)
    else:
        formulario = FormLogin(request.form)
        if formulario.validate_on_submit:
            ob_usuario = usuario('', formulario.usuario.data, '', formulario.contrasena.data)
        
        if not ob_usuario.usuario.__contains__("'") and not ob_usuario.password.__contains__("'"):
            if ob_usuario.verificar():
                session.clear
                session['user_id'] = ob_usuario.usuario
                return redirect(url_for('inicio'))    
        return render_template('InicioSesion.html', mensaje="Usuario o contraseña no valido.")

@app.route('/logout/')
@loginRequerido
def logout():
    session.clear()
    return redirect(url_for('login'))