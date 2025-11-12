document.addEventListener('DOMContentLoaded', () => {
    console.log('HBnB Frontend loaded successfully!');
    
    // Handle login form submission (Task 1)
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            await loginUser(email, password);
        });
    }
    
    // Check authentication and load places on index page (Task 2)
    const placesListSection = document.getElementById('places-list');
    if (placesListSection) {
        checkAuthentication();
        loadPriceFilter();
    }
});

// ==================== TASK 1: LOGIN FUNCTIONS ====================

async function loginUser(email, password) {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });
        
        if (response.ok) {
            const data = await response.json();
            setCookie('token', data.access_token, 7);
            window.location.href = 'index.html';
        } else {
            const errorData = await response.json();
            alert(`Login failed: ${errorData.message || 'Invalid credentials'}`);
        }
    } catch (error) {
        console.error('Error during login:', error);
        alert('An error occurred during login. Please try again.');
    }
}

// ==================== TASK 2: PLACES FUNCTIONS ====================

function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!token) {
        // Not authenticated - show login link
        if (loginLink) {
            loginLink.style.display = 'inline-block';
        }
    } else {
        // Authenticated - hide login link and fetch places
        if (loginLink) {
            loginLink.style.display = 'none';
        }
        fetchPlaces(token);
    }
}

async function fetchPlaces(token) {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/places/', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });
        
        if (response.ok) {
            const places = await response.json();
            console.log('Places fetched:', places);
            displayPlaces(places);
        } else {
            console.error('Failed to fetch places:', response.status);
            // If token is invalid, clear it and show login
            if (response.status === 401) {
                document.cookie = 'token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
                window.location.reload();
            }
        }
    } catch (error) {
        console.error('Error fetching places:', error);
    }
}

function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    placesList.innerHTML = ''; // Clear current content
    
    if (!places || places.length === 0) {
        placesList.innerHTML = '<p>No places available at the moment.</p>';
        return;
    }
    
    places.forEach(place => {
        const placeCard = document.createElement('div');
        placeCard.className = 'place-card';
        placeCard.dataset.price = place.price; // Store price for filtering

        placeCard.innerHTML = `
        <h3>${place.title || 'Unnamed Place'}</h3>
        <p><strong>Price per night:</strong> $${place.price || 'N/A'}</p>
        <p>${place.description ? place.description.substring(0, 100) + '...' : 'No description available'}</p>
        <button class="details-button" onclick="viewPlaceDetails('${place.id}')">View Details</button>
    `;

        placesList.appendChild(placeCard);
    });
}

function loadPriceFilter() {
    const priceFilter = document.getElementById('price-filter');
    
    if (!priceFilter) return;
    
    // Clear and populate price filter options
    priceFilter.innerHTML = `
        <option value="all">All Prices</option>
        <option value="10">Up to $10</option>
        <option value="50">Up to $50</option>
        <option value="100">Up to $100</option>
    `;
    
    // Add event listener for filtering
    priceFilter.addEventListener('change', (event) => {
        const selectedPrice = event.target.value;
        filterPlacesByPrice(selectedPrice);
    });
}

function filterPlacesByPrice(maxPrice) {
    const placeCards = document.querySelectorAll('.place-card');
    
    placeCards.forEach(card => {
        const price = parseFloat(card.dataset.price);
        
        if (maxPrice === 'all') {
            card.style.display = 'block';
        } else {
            const max = parseFloat(maxPrice);
            if (price <= max) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        }
    });
}

function viewPlaceDetails(placeId) {
    // Redirect to place details page
    window.location.href = `place.html?id=${placeId}`;
}

// ==================== COOKIE UTILITY FUNCTIONS ====================

function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

function getCookie(name) {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}
