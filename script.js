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

    // Simple automatic slide transition
    setInterval(() => {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }, 5000); // Change slide every 5 seconds
});
