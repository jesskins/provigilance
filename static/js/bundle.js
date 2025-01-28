$(document).ready(function() {
    $("#calendar").datepicker({
        onSelect: function() {
            $("#loading-message").hide();
        }
    });

    $("#calendar").datepicker("widget").ready(function() {
        $("#loading-message").hide();
    });

    document.getElementById('toggle-theme').addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
    });

    var backToTopButton = document.getElementById('back-to-top');
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

    var form = document.getElementById('testimonial-form');
    if (form) {
        var inputs = form.querySelectorAll('input, select, textarea');
        var clearFormButton = document.getElementById('clear-form');

        if (inputs.length > 0 && clearFormButton) {
            inputs.forEach(function(input) {
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
                inputs.forEach(function(input) {
                    input.classList.remove('valid');
                    if (input.type !== 'file') {
                        input.value = '';
                    }
                });
                form.querySelectorAll('select').forEach(function(select) {
                    select.selectedIndex = 0;
                });
                setTimeout(function() {
                    clearFormButton.classList.remove('clicked');
                }, 500);
            });
        }
    }
});
