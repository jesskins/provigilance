// search toggle
function toggleSearch() {
    const searchBar = document.getElementById('searchBar');
    if (searchBar.style.display === 'none' || searchBar.style.display === '') {
        searchBar.style.display = 'block';
    } else {
        searchBar.style.display = 'none';
    }
}


// Function to handle the request call back button
function requestCallBack() {
    window.location.href = "/request-callback/";
}


// Function to handle the request call back button
function requestCallBack() {
    window.location.href = "/request-callback/";
}

// Existing function
function toggleSearch() {
    const searchBar = document.getElementById('searchBar');
    if (searchBar.style.display === 'none' || searchBar.style.display === '') {
        searchBar.style.display = 'block';
    } else {
        searchBar.style.display = 'none';
    }
}

// New functions for the footer
document.getElementById('toggle-theme').addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
});

function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// function for form responsive design and data validation //

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('testimonial-form');
    const inputs = form.querySelectorAll('input, select, textarea');

    inputs.forEach(input => {
        input.addEventListener('input', function() {
            if (input.checkValidity()) {
                input.classList.add('valid');
            } else {
                input.classList.remove('valid');
            }
        });
    });
});


/* clear form javascript */
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('testimonial-form');
    const inputs = form.querySelectorAll('input, select, textarea');
    const clearFormButton = document.getElementById('clear-form');

    inputs.forEach(input => {
        input.addEventListener('input', function() {
            if (input.checkValidity()) {
                input.classList.add('valid');
            } else {
                input.classList.remove('valid');
            }
        });
    });

    clearFormButton.addEventListener('click', function() {
        form.reset();
        inputs.forEach(input => {
            input.classList.remove('valid');
            input.value = '';
        });
    });
});
