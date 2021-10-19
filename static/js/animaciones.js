let currentLocation = location.href;
let url = document.querySelectorAll('a');

for (let i = 0; i < url.length; i++) {
    if (url[i].href === currentLocation) {
        url[i].className = 'active';
    }
}

b