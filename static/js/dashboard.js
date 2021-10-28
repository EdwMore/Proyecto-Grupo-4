let toggle = document.querySelector('.toggle');
let navegation = document.querySelector('.navegation');
let main = document.querySelector('.main');

toggle.addEventListener('click', function () {
    navegation.classList.toggle('active');
    main.classList.toggle('active');
});

let formularioCrear = document.querySelector('.formulario');
let input = document.getElementById('nombre');
let inputArea = document.getElementById('descripcion');
let btn = document.querySelector('.formulario .btn');

let titleJugo = false;
let descripcionJugo = false;

input.addEventListener('keyup', () => {
    if (input.value.length > 0) {
        titleJugo = true;
    }
});

inputArea.addEventListener('keyup', () => {
    if (inputArea.value.length > 0) {
        descripcionJugo = true;
    } 
});

formularioCrear.addEventListener('submit', (e) => {
    if (titleJugo && descripcionJugo) {
        formularioCrear.reset();
    } else {
        e.preventDefault();
        btn.classList.add('novalidate');
    }
});