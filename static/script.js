let text = document.getElementById('text');
let leaf = document.getElementById('leaf');
let hill1 = document.getElementById('hill1');
let hill4 = document.getElementById('hill4');
let hill5 = document.getElementById('hill5');

window.addEventListener('scroll', () => {
    let value = window.scrollY;
    let sectionHeight = document.querySelector('.parallax').offsetHeight;
    let maxScrollValue = sectionHeight * 1.5;
    let adjustedScrollValue = value % maxScrollValue;

    text.style.marginTop = adjustedScrollValue * 2.5 + 'px';
    leaf.style.top = adjustedScrollValue * -0.5 + 'px';
    hill5.style.left = adjustedScrollValue * 0.5 + 'px';
    hill4.style.left = adjustedScrollValue * -0.5 + 'px';
    hill1.style.top = adjustedScrollValue * 0.25 + 'px';

    let aboutSection = document.querySelector('.sec');
    let sectionTop = aboutSection.offsetTop;
    let sectionBottom = sectionTop + aboutSection.offsetHeight;
    let windowBottom = window.pageYOffset + window.innerHeight;
    if (windowBottom > sectionTop && window.pageYOffset < sectionBottom) {
        document.querySelector('.sec h2').style.transform = 'translateX(0)';
        document.querySelector('.sec p').style.transform = 'translateX(0)';
    } else {
        document.querySelector('.sec h2').style.transform = 'translateX(-200%)';
        document.querySelector('.sec p').style.transform = 'translateX(200%)';
    }
});
