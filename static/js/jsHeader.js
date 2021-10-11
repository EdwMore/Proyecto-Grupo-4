let active = document.querySelectorAll('.nav__li');
console.log(active);

//Recorre el vector.
active.forEach(element => { /* element, es como una variable, donde se guarda cada elemento del vector */
    element.addEventListener('click', function () { /* Evento escucha al hacer click */
        active.forEach(nav => nav.classList.remove('active')); /* Quita la clase 'active' si existe */

        this.classList.add('active'); /* Si no exite la coloca */
    });
});

