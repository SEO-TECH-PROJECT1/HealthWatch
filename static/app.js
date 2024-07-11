// File: File: HealthWatch/static/app.js
// Example JavaScript for enhancing form validation and interactivity

document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            if (username.length === 0 || password.length === 0) {
                alert('Please fill in both username and password.');
                event.preventDefault();
            }
        });
    }
});

