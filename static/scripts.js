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
