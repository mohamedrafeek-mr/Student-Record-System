# Student Record Submission System - Setup & Configuration Guide

## Quick Start

### 1. Installation
The Django project is already set up and configured. Database migrations have been applied.

### 2. Start the Development Server
```bash
cd "c:\Users\Admin\OneDrive\Desktop\Django Project\srspro"
py manage.py runserver
```

### 3. Access the Application
Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

## Test User Credentials

Use any of these accounts to test the application:

| Username | Password | Assignments |
|----------|----------|------------|
| john_doe | password123 | 3 assignments (1 submitted, 2 pending) |
| jane_smith | pass456 | 2 assignments (1 submitted, 1 pending) |
| alice_jones | alice789 | 2 assignments (both pending) |

## Admin Panel Access

### 1. Create Superuser (if needed)
```bash
py manage.py createsuperuser
```
Follow the prompts to create admin credentials.

### 2. Access Admin Panel
Navigate to:
```
http://127.0.0.1:8000/admin/
```

## Useful Django Commands

### Database Management
```bash
# Create migrations for changes
py manage.py makemigrations

# Apply migrations to database
py manage.py migrate

# View migration status
py manage.py showmigrations

# Reset database (WARNING: Deletes all data)
py manage.py flush
```

### Testing & Debugging
```bash
# Run Django's system checks
py manage.py check

# Enter Python shell with Django context
py manage.py shell

# Collect static files
py manage.py collectstatic
```

### Data Management
```bash
# Populate test data
py manage.py populate_test_data

# Clear and repopulate test data
py manage.py populate_test_data --clear

# Export data to fixture
py manage.py dumpdata srsapp > data.json

# Load data from fixture
py manage.py loaddata data.json
```

## Project Configuration Files

### settings.py
Contains all Django configuration:
- Installed apps: admin, auth, contenttypes, sessions, messages, staticfiles, srsapp
- Database configuration: SQLite
- Templates directory: srsapp/templates
- Static files: srsapp/static

### urls.py
URL routing:
- Login: /login/
- Home: /home/
- Submit: /submit/<assignment_id>/
- Logout: /logout/
- Admin: /admin/

## Database Structure

### Users Table (users)
```
id: Integer (Primary Key)
username: String (Unique)
password: String
```

### Assignments Table (assignments)
```
assignment_id: Integer (Primary Key, Auto-increment)
username: Foreign Key (references users.username)
assignment_name: String
submitted_status: String (Not Submitted / Submitted)
submitted_time: DateTime (nullable)
```

## File Structure Summary

```
srspro/
├── README.md                 # Main project documentation
├── SETUP.md                  # This file
├── requirements.txt          # Python dependencies
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── srspro/                  # Project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL configuration
│   ├── wsgi.py              # Production WSGI config
│   └── asgi.py              # Async ASGI config
└── srsapp/                  # Main application
    ├── models.py            # User & Assignment models
    ├── views.py             # Login, Home, Submit views
    ├── urls.py              # App URL patterns
    ├── admin.py             # Admin site configuration
    ├── apps.py              # App configuration
    ├── migrations/          # Database migrations
    ├── management/          # Custom management commands
    │   └── commands/
    │       └── populate_test_data.py
    ├── templates/           # HTML templates
    │   ├── login.html       # Login page
    │   ├── home.html        # Assignment list
    │   └── submit.html      # Submission form
    └── static/              # CSS, JS, Images
        ├── css/
        │   └── style.css    # Custom styling
        └── js/
            └── loader.js    # AJAX utilities
```

## Common Issues & Solutions

### Issue: Port 8000 already in use
```bash
# Use different port
py manage.py runserver 8001
```

### Issue: Static files not loading
```bash
# Collect static files
py manage.py collectstatic --noinput
```

### Issue: Template not found
1. Verify templates directory exists: `srsapp/templates/`
2. Check TEMPLATES setting in settings.py
3. Restart development server

### Issue: Database locked
```bash
# Reset database
py manage.py flush
py manage.py populate_test_data
```

### Issue: Migration conflicts
```bash
# Show all migrations
py manage.py showmigrations

# Reset migrations (danger - data loss)
py manage.py migrate srsapp zero
py manage.py migrate
```

## Security Considerations

### For Development
- DEBUG = True (enabled for development)
- SECRET_KEY: Change in production
- ALLOWED_HOSTS: Add your domain in production

### For Production
1. Set DEBUG = False
2. Change SECRET_KEY in settings.py
3. Use environment variables for sensitive data
4. Configure ALLOWED_HOSTS
5. Use HTTPS
6. Set secure database password
7. Use PostgreSQL instead of SQLite
8. Enable CSRF protection (already enabled)
9. Configure CORS if needed

## Environment Setup

### Windows PowerShell
```powershell
# Navigate to project
cd "c:\Users\Admin\OneDrive\Desktop\Django Project\srspro"

# Run server
py manage.py runserver
```

### Linux/Mac Terminal
```bash
# Navigate to project
cd path/to/srspro

# Run server
python manage.py runserver
```

## Performance Tips

1. **Database Queries**: Use `select_related()` and `prefetch_related()` for foreign keys
2. **Static Files**: Enable browser caching in production
3. **Sessions**: Consider Redis for session storage
4. **Middleware**: Only enable necessary middleware
5. **Database**: Migrate to PostgreSQL for production

## Deployment Checklist

- [ ] Set DEBUG = False
- [ ] Change SECRET_KEY
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up database (PostgreSQL recommended)
- [ ] Configure static files collection
- [ ] Enable HTTPS
- [ ] Set up email backend for notifications
- [ ] Configure logging
- [ ] Set up monitoring
- [ ] Backup database strategy
- [ ] Load balancing setup
- [ ] CDN configuration

## Additional Resources

- Django Documentation: https://docs.djangoproject.com/
- Bootstrap Documentation: https://getbootstrap.com/docs/
- SQLite vs PostgreSQL: https://www.postgresql.org/
- Django Best Practices: https://docs.djangoproject.com/en/stable/intro/

## Support

For issues or questions:
1. Check the README.md for feature documentation
2. Review Django official documentation
3. Check console error messages
4. Verify database connectivity
5. Review logs in development mode

---

**Version**: 1.0  
**Last Updated**: February 2026
