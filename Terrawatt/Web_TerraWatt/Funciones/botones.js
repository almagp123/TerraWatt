
    const slider = document.querySelector('.reseñas-slider');
    const btnPrev = document.getElementById('goPrevious');
    const btnNext = document.getElementById('goNext');

    let currentIndex = 0;

    btnNext.addEventListener('click', () => {
        const totalItems = slider.children.length;
        if (currentIndex < totalItems - 1) {
            currentIndex++;
            updateSliderPosition();
        }
    });

    btnPrev.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            updateSliderPosition();
        }
    });

    function updateSliderPosition() {
        const itemWidth = slider.children[0].clientWidth + 20; // El 20 es el gap entre reseñas
        slider.style.transform = `translateX(${-currentIndex * itemWidth}px)`;
    }


