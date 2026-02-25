// Loader JavaScript - AJAX and jQuery utilities

// Show loader
function showLoader() {
    const loader = document.getElementById('loader');
    if (loader) {
        loader.style.display = 'flex';
    }
}

// Hide loader
function hideLoader() {
    const loader = document.getElementById('loader');
    if (loader) {
        loader.style.display = 'none';
    }
}

// Simulate AJAX loader for form submission
document.addEventListener('DOMContentLoaded', function() {
    // Handle form submissions with loader
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            // Show loader for important forms (excluding some)
            if (!this.classList.contains('no-loader')) {
                // Optional: uncomment to show loader on form submit
                // showLoader();
            }
        });
    });

    // Hide loader after page load
    window.addEventListener('load', hideLoader);

    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            // bsAlert.close(); // Uncomment to auto-close alerts
        }, 5000);
    });
});

// AJAX helper function for loading content
function loadContent(url, element) {
    showLoader();
    fetch(url)
        .then(response => response.text())
        .then(data => {
            if (element) {
                document.querySelector(element).innerHTML = data;
            }
            hideLoader();
        })
        .catch(error => {
            console.error('Error loading content:', error);
            hideLoader();
        });
}

// Handle navigation with AJAX
function navigateTo(url) {
    showLoader();
    window.location.href = url;
}

// jQuery compatibility (if jQuery is included)
if (typeof jQuery !== 'undefined') {
    jQuery(document).ready(function($) {
        // jQuery AJAX utilities
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                // Add loading indicator
                // showLoader(); - uncomment if needed
            },
            complete: function() {
                // hideLoader(); - uncomment if needed
            }
        });

        // Tooltip initialization
        $('[data-bs-toggle="tooltip"]').tooltip();

        // Popover initialization
        $('[data-bs-toggle="popover"]').popover();
    });
}

// Loading animation for buttons
function setButtonLoading(buttonSelector, isLoading = true) {
    const btn = document.querySelector(buttonSelector);
    if (btn) {
        if (isLoading) {
            btn.disabled = true;
            btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Loading...';
        } else {
            btn.disabled = false;
            btn.innerHTML = 'Submit';
        }
    }
}

// Confirm action before deletion or important operations
function confirmAction(message = 'Are you sure?') {
    return confirm(message);
}

// Format datetime
function formatDateTime(dateString) {
    const options = {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    };
    return new Date(dateString).toLocaleDateString('en-US', options);
}

// Validation helper
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (form && form.checkValidity() === false) {
        event.preventDefault();
        event.stopPropagation();
        form.classList.add('was-validated');
        return false;
    }
    return true;
}

// Session timeout warning
function initSessionTimeout(timeoutMinutes = 60) {
    const timeoutMs = timeoutMinutes * 60 * 1000;
    
    setTimeout(() => {
        if (confirm('Your session is about to expire. Do you want to continue?')) {
            // Keep session alive
            fetch('{% url "home" %}').catch(err => console.log('Keep alive ping'));
            initSessionTimeout(timeoutMinutes);
        } else {
            // Redirect to logout
            window.location.href = '{% url "logout" %}';
        }
    }, timeoutMs - 60000); // 1 minute before actual timeout
}

// Utility to disable submit button to prevent multiple submissions
function preventDoubleSubmit(formId) {
    const form = document.getElementById(formId);
    if (form) {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.textContent = 'Submitting...';
            }
        });
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    // Prevent double submit on all forms
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        preventDoubleSubmit(form.id);
    });
});

console.log('Loader.js loaded successfully');
