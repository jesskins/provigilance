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

// New functions for the footer
document.getElementById('toggle-theme').addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
});

function scrollToTop() {
    window.scrollTo({ 
        top: 0, behavior: 'smooth' 
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('testimonial-form');
    const inputs = form.querySelectorAll('input, select, textarea');
    const clearFormButton = document.getElementById('clear-form');

    // Add event listener for form inputs to validate fields
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            if (input.checkValidity()) {
                input.classList.add('valid');
            } else {
                input.classList.remove('valid');
            }
        });
    });

    // Add event listener for the clear form button
    clearFormButton.addEventListener('click', function() {
        clearFormButton.classList.add('clicked');

        // Reset the form
        form.reset();

        // Clear validation styles and input values
        inputs.forEach(input => {
            input.classList.remove('valid');
            if (input.type !== 'file') {
                input.value = '';
            }
        });

        // Reset select fields
        form.querySelectorAll('select').forEach(select => select.selectedIndex = 0);

        // Remove the 'clicked' class after animation ends
        setTimeout(() => {
            clearFormButton.classList.remove('clicked');
        }, 500); // Adjust duration if needed
    });
});

// for the calendar of booking page //

// Import FullCalendar and necessary plugins
import { Calendar } from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';
import interactionPlugin from '@fullcalendar/interaction';

// Function to initialize the calendar
function initializeCalendar() {
    var calendarEl = document.getElementById('calendar');

    if (!calendarEl) {
        console.error('Calendar element not found');
        return;
    }

    // Fetch events from the data attribute and handle empty JSON cases
    var eventsData = calendarEl.dataset.events;
    var events;

    try {
        events = JSON.parse(eventsData);
        if (!events) {
            throw new Error("Events data is null or empty");
        }
    } catch (e) {
        events = [];
        console.error('Invalid JSON data for events:', e);
    }

    console.log('Events:', events);

    if (typeof Calendar !== 'undefined') {
        var calendar = new Calendar(calendarEl, {
            plugins: [dayGridPlugin, interactionPlugin],
            initialView: 'dayGridMonth',
            events: events,
            headerToolbar: {
                left: 'prev,next today',
                center: 'title',
                right: 'dayGridMonth,timeGridWeek,timeGridDay'
            },
            selectable: true,
            selectHelper: true
        });

        calendar.render();
    } else {
        console.error('FullCalendar is not defined');
    }
}

// Call the function to initialize the calendar after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', initializeCalendar);
