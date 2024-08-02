document.addEventListener('DOMContentLoaded', function() {
    const slider = document.querySelector('.slider');
    const slides = document.querySelectorAll('.cust_bot');
    const prev = document.getElementById('prev');
    const next = document.getElementById('next');

    let currentIndex = 0;

    function showSlide(index) {
        const slideWidth = slides[0].clientWidth + 20; 
        slider.style.transform = `translateX(-${index * slideWidth}px)`;
    }

    prev.addEventListener('click', function() {
        if (currentIndex > 0) {
            currentIndex--;
            showSlide(currentIndex);
        }
    });

    next.addEventListener('click', function() {
        if (currentIndex < slides.length - 3) {
            currentIndex++;
            showSlide(currentIndex);
        }
    });
    window.addEventListener('resize', function() {
        showSlide(currentIndex);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.getElementById('hamburger');
    const navbot = document.querySelector('.navbot');

    hamburger.addEventListener('click', function() {
        navbot.classList.toggle('show');
        hamburger.classList.toggle('active');
    });
});
