const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario .input');

const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	password: /^.{4,12}$/, // 4 a 12 digitos.
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{7,14}$/ // 7 a 14 numeros.
}

const campos = {
    nombre: false,
    correo: false,
    usuario: false,
    contrasena: false
}

const validarFormulario = (e) => {
    switch (e.target.name) {
        case "nombre":
            validarCampo(expresiones.nombre, e.target, 'nombre');
        break
        case "correo":
            validarCampo(expresiones.correo, e.target, 'correo');
        break
        case "usuario":
            validarCampo(expresiones.usuario, e.target, 'usuario');
        break
        case "contrasena":
            validarCampo(expresiones.password, e.target, 'contrasena');
        break
    }
}

const validarCampo = (expresion, input, campo) => {
    if (expresion.test(input.value)) {
        document.querySelector(`#${campo} .validate`).classList.remove('error');
        document.querySelector(`#${campo} .validate`).classList.add('activo');
        document.querySelectorAll(`#${campo} i`)[1].classList.remove('fa-times');
        document.querySelectorAll(`#${campo} i`)[1].classList.add('fa-check');
        document.querySelector(`#${campo} span`).classList.remove('activo');
        campos[campo] = true;
    } else {
        document.querySelector(`#${campo} .validate`).classList.remove('activo');
        document.querySelector(`#${campo} .validate`).classList.add('error');
        document.querySelectorAll(`#${campo} i`)[1].classList.remove('fa-check');
        document.querySelectorAll(`#${campo} i`)[1].classList.add('fa-times');
        document.querySelector(`#${campo} span`).classList.add('activo');
        campos[campo] = false;
    }
}

inputs.forEach((input => {
    input.addEventListener('keyup', validarFormulario);
}))

formulario.addEventListener('submit', (e) => {

    if (!(campos.nombre && campos.correo && campos.usuario && campos.contrasena)) {
        e.preventDefault();
    } 
});