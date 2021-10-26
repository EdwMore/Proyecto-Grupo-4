const fav = document.querySelectorAll('.contenedor__contenido-img i');

fav.forEach(element => {
    element.addEventListener('click', () => {
        element.classList.toggle('activo');
    });
});

const size = document.querySelectorAll('.contenedor__contenido-descripcion .size span');

size.forEach(element => {
    element.addEventListener('click', function () {
        size.forEach(element2 => element2.classList.remove('activo'));
        this.classList.add('activo');
    });
});