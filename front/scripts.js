/* 
  HBnB Frontend - JavaScript
  Task 1: Login Functionality
  Task 2: List of Places
  Task 3: Place Details
  Task 4: Add Review
*/

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

    // Check if we're on the place details page (Task 3)
    const placeDetailsSection = document.getElementById('place-details');
    if (placeDetailsSection) {
        const placeId = getPlaceIdFromURL();
        if (placeId) {
            checkAuthenticationForPlace(placeId);
        } else {
            placeDetailsSection.innerHTML = '<p>Error: No place ID provided.</p>';
        }
    }

    // Setup review form submission (Task 4)
    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
        reviewForm.addEventListener('submit', async (event) => {
            event.preventDefault();

            const token = getCookie('token');
            if (!token) {
                alert('You must be logged in to submit a review.');
                window.location.href = 'login.html';
                return;
            }

            const placeId = getPlaceIdFromURL();
            if (!placeId) {
                alert('Error: No place ID found.');
                return;
            }

            const rating = document.getElementById('rating').value;
            const reviewText = document.getElementById('review-text').value;

            if (!rating || !reviewText) {
                alert('Please provide both a rating and review text.');
                return;
            }

            await submitReview(token, placeId, rating, reviewText);
        });
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

// ==================== TASK 3: PLACE DETAILS FUNCTIONS ====================

function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
}

function checkAuthenticationForPlace(placeId) {
    const token = getCookie('token');
    const addReviewSection = document.getElementById('add-review');

    if (!token) {
        // Not authenticated - hide review form
        if (addReviewSection) {
            addReviewSection.style.display = 'none';
        }
        // Fetch place details without token (if your API allows it)
        fetchPlaceDetails(null, placeId);
    } else {
        // Authenticated - show review form
        if (addReviewSection) {
            addReviewSection.style.display = 'block';
        }
        // Fetch place details with token
        fetchPlaceDetails(token, placeId);
    }
}

async function fetchPlaceDetails(token, placeId) {
    try {
        const headers = {
            'Content-Type': 'application/json'
        };

        // Add token to headers if available
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }

        const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
            method: 'GET',
            headers: headers
        });

        if (response.ok) {
            const place = await response.json();
            console.log('Place details fetched:', place);
            displayPlaceDetails(place);
        } else {
            console.error('Failed to fetch place details:', response.status);
            document.getElementById('place-details').innerHTML =
                '<p>Error loading place details. Please try again later.</p>';
        }
    } catch (error) {
        console.error('Error fetching place details:', error);
        document.getElementById('place-details').innerHTML =
            '<p>Error loading place details. Please try again later.</p>';
    }
}

function displayPlaceDetails(place) {
    const placeDetailsSection = document.getElementById('place-details');
    placeDetailsSection.innerHTML = ''; // Clear current content

    // Create place details HTML
    const placeInfo = document.createElement('div');
    placeInfo.className = 'place-info';

    placeInfo.innerHTML = `
        <h1>${place.title || 'Unnamed Place'}</h1>
        <p class="place-price"><strong>Price per night:</strong> $${place.price || 'N/A'}</p>
        <p class="place-description">${place.description || 'No description available.'}</p>
        <p class="place-location"><strong>Location:</strong> Latitude ${place.latitude}, Longitude ${place.longitude}</p>
        <p class="place-host"><strong>Host:</strong> ${place.owner?.first_name || 'Unknown'} ${place.owner?.last_name || ''}</p>
    `;

    placeDetailsSection.appendChild(placeInfo);

    // Display amenities
    if (place.amenities && place.amenities.length > 0) {
        const amenitiesSection = document.createElement('div');
        amenitiesSection.className = 'amenities-section';
        amenitiesSection.innerHTML = '<h2>Amenities</h2>';

        const amenitiesList = document.createElement('ul');
        amenitiesList.className = 'amenities-list';

        place.amenities.forEach(amenity => {
            const li = document.createElement('li');
            li.textContent = amenity.name;
            amenitiesList.appendChild(li);
        });

        amenitiesSection.appendChild(amenitiesList);
        placeDetailsSection.appendChild(amenitiesSection);
    }

    // Display reviews
    displayReviews(place.reviews || []);
}

function displayReviews(reviews) {
    const reviewsSection = document.createElement('div');
    reviewsSection.className = 'reviews-section';
    reviewsSection.innerHTML = '<h2>Reviews</h2>';

    if (!reviews || reviews.length === 0) {
        reviewsSection.innerHTML += '<p>No reviews yet. Be the first to review!</p>';
    } else {
        reviews.forEach(review => {
            const reviewCard = document.createElement('div');
            reviewCard.className = 'review-card';

            reviewCard.innerHTML = `
                <p class="review-user"><strong>${review.user?.first_name || 'Anonymous'} ${review.user?.last_name || ''}</strong></p>
                <p class="review-rating">Rating: ${'⭐'.repeat(review.rating || 0)}</p>
                <p class="review-text">${review.text || 'No comment provided.'}</p>
                <p class="review-date"><em>${new Date(review.created_at).toLocaleDateString()}</em></p>
            `;

            reviewsSection.appendChild(reviewCard);
        });
    }

    document.getElementById('place-details').appendChild(reviewsSection);
}

// ==================== TASK 4: ADD REVIEW FUNCTIONS ====================

async function submitReview(token, placeId, rating, reviewText) {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/reviews/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({
                place_id: placeId,
                rating: parseInt(rating),
                text: reviewText
            })
        });

        if (response.ok) {
            const data = await response.json();
            console.log('Review submitted:', data);
            alert('Review submitted successfully!');

            // Clear the form
            document.getElementById('rating').value = '';
            document.getElementById('review-text').value = '';

            // Reload place details to show the new review
            checkAuthenticationForPlace(placeId);
        } else {
            const errorData = await response.json();
            console.error('Failed to submit review:', errorData);
            alert(`Failed to submit review: ${errorData.message || 'Unknown error'}`);
        }
    } catch (error) {
        console.error('Error submitting review:', error);
        alert('An error occurred while submitting the review. Please try again.');
    }
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
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}
