let toggle = document.querySelector('.toggle');
let navegation = document.querySelector('.navegation');
let main = document.querySelector('.main');

toggle.addEventListener('click', function () {
    navegation.classList.toggle('active');
    main.classList.toggle('active');
});




let list = document.querySelectorAll('.navegation li');
function activeLink() {
    list.forEach((item) => item.classList.remove('hovered'));
    this.classList.add('hovered')
}
list.forEach((item => item.addEventListener('mouseover', activeLink)))