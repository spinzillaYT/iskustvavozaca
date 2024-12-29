document.addEventListener('DOMContentLoaded', () => {
    // Animate rating number
    const ratingNumber = document.querySelector('.rating-number');
    if (ratingNumber) {
        const finalRating = parseFloat(ratingNumber.textContent);
        ratingNumber.textContent = '0';
        
        let currentRating = 0;
        const duration = 2000; // 2 seconds
        const steps = 60;
        const increment = finalRating / steps;
        const stepDuration = duration / steps;

        const counter = setInterval(() => {
            currentRating += increment;
            if (currentRating >= finalRating) {
                currentRating = finalRating;
                clearInterval(counter);
            }
            ratingNumber.textContent = currentRating.toFixed(1);
        }, stepDuration);
    }

    // Animate progress bars when they come into view
    const progressBars = document.querySelectorAll('.progress-bar');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const progressBar = entry.target;
                const width = progressBar.getAttribute('aria-valuenow') + '%';
                progressBar.style.width = '0%';
                
                // Force a reflow
                progressBar.offsetHeight;
                
                // Add animation class
                progressBar.style.transition = 'width 1.5s ease-out';
                progressBar.style.width = width;
                
                observer.unobserve(progressBar);
            }
        });
    }, { threshold: 0.2 });

    progressBars.forEach(bar => observer.observe(bar));
});
