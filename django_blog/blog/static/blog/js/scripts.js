// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', function() {
    
    // alert messages auto-hide after a few seconds
    const forms = document.querySelectorAll('.success-message', '.error-message');
    meessages.forEach(message => {
        setTimeout(() => {
            message.style.display = 'none';
        }, 5000); // hide after 5 seconds
    });

    //validate search form for non-empty submission
    const searchForm = document.querySelector(form[action*="post-list"]);
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            const queryInput = searchForm.querySelector('input[name="q"]');
            if (queryInput && queryInput.value.trim() === '') {
                e.preventDefault();
                alert('Please enter a search term.');
            }
        });
    }
    // highlight active nav link
    const navLinks = document.querySelectorAll('.nav a');
    const currentUrl = window.location.href;
    navLinks.forEach(link => {
        if (currentUrl.includes(link.href)) {
            link.style.fontWeight = 'bold';
            link.style.textDecoration = 'underline';
        }
    });
});