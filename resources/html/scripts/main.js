const titles = [
    'Ward Finder',
    'Visitor Registration',
    'Hospital Navigator'
];

const rotatingElement = document.getElementById('rotating-text');

rotatingElement.textContent = titles[0];

let currentIndex = 0;

function updateRotatingText(){

    rotatingElement.style.opacity = 0;

    setTimeout(() => {
        currentIndex = (currentIndex + 1) % titles.length;
        rotatingElement.textContent = titles[currentIndex]; 
        rotatingElement.style.opacity = 1;
    },1000);
}
setInterval(updateRotatingText, 3000)