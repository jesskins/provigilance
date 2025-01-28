$(document).ready(function() {
    // Initialize jQuery UI Datepicker on the calendar element
   $("#calendar").datepicker({
        // Customize the datepicker options if needed
   });

// Function to toggle search bar visibility
function toggleSearch() {
    const searchBar = document.getElementById('searchBar');
    console.log('toggleSearch function called'); // Debugging log
    if (searchBar.style.display === 'none' || searchBar.style.display === '') {
        searchBar.style.display = 'block';
    } else {
        searchBar.style.display = 'none';
    }
}

// Use jQuery's $(document).ready() to ensure the DOM is fully loaded
$(document).ready(function() {
    console.log('$(document).ready event fired'); // Debugging log
    const toggleButton = document.getElementById('searchIcon');
    if (toggleButton) {
        console.log('Adding click event listener to searchIcon'); // Debugging log
        toggleButton.addEventListener('click', toggleSearch);
    } else {
        console.log('searchIcon element not found'); // Debugging log
    }
});

    
    // Function to handle the request call back button
    function requestCallBack() {
        window.location.href = "/request-callback/";
    }

    // New functions for the footer
    document.getElementById('toggle-theme').addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
    });

    // "Back to Top" button functionality
    const backToTopButton = document.getElementById('back-to-top');

    backToTopButton.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });

    const form = document.getElementById('testimonial-form');
    if (form) {
        const inputs = form.querySelectorAll('input, select, textarea');
        const clearFormButton = document.getElementById('clear-form');

        if (inputs.length > 0 && clearFormButton) {
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
                clearFormButton.classList.add('clicked');

                form.reset();

                inputs.forEach(input => {
                    input.classList.remove('valid');
                    if (input.type !== 'file') {
                        input.value = '';
                    }
                });

                form.querySelectorAll('select').forEach(select => select.selectedIndex = 0);

                setTimeout(() => {
                    clearFormButton.classList.remove('clicked');
                }, 500);
            });
        }
    }
});

// Initialize jQuery UI Datepicker on the calendar element
$(document).ready(function() {
    $("#calendar").datepicker({
        onSelect: function() {
            $("#loading-message").hide();
        }
    });

    // Hide the loading message once the datepicker is ready
    $("#calendar").datepicker("widget").ready(function() {
        $("#loading-message").hide();
    });
});
