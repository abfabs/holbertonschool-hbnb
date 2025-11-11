document.addEventListener('DOMContentLoaded', () => {
    console.log('HBnB Frontend loaded successfully!');

    // Handle login form submission
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();

            // Get form values
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            // Call login function
            await loginUser(email, password);
        });
    }
});

// Function to handle login API call
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

            // Store JWT token in cookie
            setCookie('token', data.access_token, 7); // Cookie expires in 7 days

            // Redirect to main page
            window.location.href = 'index.html';
        } else {
            // Handle login failure
            const errorData = await response.json();
            alert(`Login failed: ${errorData.message || 'Invalid credentials'}`);
        }
    } catch (error) {
        console.error('Error during login:', error);
        alert('An error occurred during login. Please try again.');
    }
}

// Function to set a cookie
function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

// Function to get a cookie by name
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

// Function to check if user is authenticated
function checkAuthentication() {
    const token = getCookie('token');
    return token !== null;
}
