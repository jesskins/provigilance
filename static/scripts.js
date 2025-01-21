// Ensure the document is ready
$(document).ready(function() {
    // Initialize jQuery UI Datepicker on the calendar element
    $("#calendar").datepicker({
        // Customize the datepicker options if needed
    });

    // Function to toggle search bar visibility
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

    // New functions for the footer
    document.getElementById('toggle-theme').addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
    });

    function scrollToTop() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

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
