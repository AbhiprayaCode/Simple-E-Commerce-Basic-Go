document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.testimonial-item');
    let currentSlide = 0;

    console.log('Slides:', slides);
    
    function showSlide(index) {
        console.log('Showing slide:', index);
        slides.forEach((slide, i) => {
            slide.style.transform = `translateX(${(i - index) * 100}%)`;
        });
    }

    setInterval(() => {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }, 5000);
});

document.addEventListener('DOMContentLoaded', () => {
    const products = document.querySelectorAll('.product-card');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show'); 
            }
        });
    }, {
        threshold: 0.2 
    });

    products.forEach(product => {
        observer.observe(product);
    });
});

