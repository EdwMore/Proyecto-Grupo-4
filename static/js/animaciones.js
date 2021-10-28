let currentLocation = location.href;
let url = document.querySelectorAll('.enlaces');

for (let i = 0; i < url.length; i++) {
    if (url[i].href === currentLocation) {
        url[i].className = 'active';
    }
}

let LocationCurrent = location.href;
let url2 = document.querySelectorAll('.enlaces2');
let lista = document.querySelectorAll('.navegation li')

for (let i = 0; i < url2.length; i++) {
    if (url2[i].href === LocationCurrent) {
        lista[i].classList.toggle('hovered');
    }
}