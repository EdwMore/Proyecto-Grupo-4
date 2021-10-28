import os
import functools 

from flask import Flask, render_template, request, url_for, g, session
from werkzeug.utils import redirect
from forms import FormCrearJugo, FormLogin, FormRegistro
from models import usuario, Jugo

app = Flask(__name__)

app.config['SECRET_KEY'] = "bfc16d88366b75ca826ee9f01407d02e6628975c8b3faf358bcf508703d972b8p"

def loginRequerido(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login'))
        
        return view(**kwargs)
    
    return wrapped_view

def UserLogueado(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is not None:
            return redirect(url_for('Inicio'))
        
        return view(**kwargs)

    return wrapped_view

def Administrador(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is not None:
            if g.user.usuario == "ElPepe":
                return view(**kwargs)
        
        return redirect(url_for('Inicio'))
    
    return wrapped_view

@app.before_request
def UsuarioAutentico():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else: 
        g.user = usuario.cargar(user_id)

@app.route('/inicio/')
def Inicio():
    title = 'Inicio'
    return render_template('Inicio.html', title=title)

@app.route('/')
def Header():
    return redirect(url_for('Inicio'))

@app.route('/registro/', methods=["GET", "POST"])
@UserLogueado
def registro():
    title = "Registro"
    if request.method == "GET":
        formulario = FormRegistro()
        return render_template('Registro.html', title=title, form=formulario)
    else:
        formulario = FormRegistro(request.form)
        if formulario.validate_on_submit():
            ob_usuario = usuario(formulario.nombre.data, formulario.usuario.data, formulario.correo.data, formulario.contrasena.data)
            if ob_usuario.insertar():
                return render_template('Registro.html', exito="Se ha registrado su cuenta.")

        return render_template('Registro.html', title=title, form=formulario)

@app.route('/login/', methods=["GET", "POST"])
@UserLogueado
def login():
    title = "Inicio Sesion"
    if request.method == "GET":
        formulario = FormLogin()
        return render_template('InicioSesion.html', title=title ,form=formulario)
    else:
        formulario = FormLogin(request.form)
        if formulario.validate_on_submit():
            ob_usuario = usuario('', formulario.usuario.data, '', formulario.contrasena.data)
        
        if not ob_usuario.usuario.__contains__("'") and not ob_usuario.password.__contains__("'"):
            if ob_usuario.verificar():
                session.clear
                session['user_id'] = ob_usuario.usuario
                if ob_usuario.usuario == "ElPepe":
                    return redirect(url_for('dashboard'))
                else:
                    return redirect(url_for('Inicio'))  

        return render_template('InicioSesion.html', title=title ,mensaje="Usuario o contraseña no valido.", form=formulario)

@app.route('/jugos/')
@loginRequerido
def jugos():
    return render_template('VistasJugos.html', title='Jugos', listaJugos=Jugo.listadoJugos())

@app.route('/dashboard/')
@Administrador
def dashboard():
    return render_template('Dashboard.html', title="Dashboard", listaUsuarios=usuario.listadoUsuarios())

@app.route('/crearjugo/', methods=["GET", "POST"])
def crearJugo():
    title="Crear Jugo"
    if request.method == "GET":
        formulario = FormCrearJugo()
        return render_template('CrearJugo.html', title=title ,form=formulario)
    else:
        formulario = FormCrearJugo(request.form)
        if formulario.validate_on_submit():
            ob_jugo = Jugo(formulario.nombre.data, formulario.descripcion.data)
        if not ob_jugo.nombre.__contains__("'") and not ob_jugo.descripcion.__contains__("'"):
            if ob_jugo.insertar():
                return render_template("CrearJugo.html", exito="Su jugo fue creado", form=formulario)

        return render_template('CrearJugo.html', title=title, form=formulario)

@app.route('/logout/')
@loginRequerido
def logout():
    session.clear()
    return redirect(url_for('Inicio'))
