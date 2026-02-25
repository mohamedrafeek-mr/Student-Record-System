# Student Record Submission System - Django

A complete Student Record Submission Web Application using Django framework where students can log in, view assigned assignments, and submit their assignments online.

## Project Features

✅ **User Authentication**
- Session-based login system
- Only predefined users can log in (no new user registration)
- Secure password validation

✅ **Assignment Management**
- Display assignments assigned to each user
- View assignment details with submission status
- Real-time submission tracking

✅ **Assignment Submission**
- Simple and intuitive submission interface
- Track submission status (Not Submitted / Submitted)
- Display submission date and time

✅ **User Interface**
- Bootstrap-based responsive design
- Mobile-friendly layout
- Interactive animations and loaders
- Clean and professional appearance

✅ **Security**
- Session-based authentication
- Decorators for page access protection
- Session validation on every protected page
- Prevents unauthorized access via URL

## Technology Stack

- **Backend**: Django 6.0.2
- **Frontend**: HTML, CSS, Bootstrap 5.1.3
- **Database**: SQLite
- **Session Management**: Django Sessions
- **Client-side**: JavaScript, jQuery (optional)

## Project Structure

```
srspro/
├── manage.py                      # Django management script
├── db.sqlite3                     # SQLite database
├── srspro/                        # Project settings folder
│   ├── settings.py               # Django settings
│   ├── urls.py                   # URL routing
│   ├── wsgi.py                   # WSGI configuration
│   └── asgi.py                   # ASGI configuration
└── srsapp/                        # Main application folder
    ├── models.py                 # Database models (User, Assignment)
    ├── views.py                  # Application views
    ├── admin.py                  # Django admin configuration
    ├── urls.py                   # App URL routing
    ├── migrations/               # Database migrations
    ├── templates/                # HTML templates
    │   ├── login.html           # Login page
    │   ├── home.html            # Assignment list page
    │   └── submit.html          # Assignment submission page
    └── static/                   # Static files
        ├── css/
        │   └── style.css        # Custom CSS
        └── js/
            └── loader.js        # JavaScript utilities
```

## Database Schema

### Users Table
```sql
id          INTEGER PRIMARY KEY
username    VARCHAR(100) UNIQUE
password    VARCHAR(255)
```

### Assignments Table
```sql
assignment_id       INTEGER PRIMARY KEY
username            FOREIGN KEY (users.username)
assignment_name     VARCHAR(255)
submitted_status    VARCHAR(50) (Not Submitted / Submitted)
submitted_time      DATETIME (nullable)
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- Django 6.0.2
- pip (Python package manager)

### Step 1: Navigate to Project Directory
```bash
cd "c:\Users\Admin\OneDrive\Desktop\Django Project\srspro"
```

### Step 2: Install Dependencies (Optional)
```bash
pip install django
```

### Step 3: Apply Database Migrations
Migrations are already configured. No further action needed.

### Step 4: Create Test Users (Already Done)
The following test users are already created:
- **Username**: john_doe, **Password**: password123
- **Username**: jane_smith, **Password**: pass456
- **Username**: alice_jones, **Password**: alice789

### Step 5: Run Development Server
```bash
py manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## Usage Guide

### Login Page
1. Navigate to the application URL
2. Enter your username and password
3. Click "Login"
4. If credentials are correct, you'll be redirected to the home page

### Home Page (Dashboard)
1. View all your assigned assignments
2. Check the submission status of each assignment
3. See detailed information about each assignment:
   - Assignment ID
   - Assignment Name
   - Current Status (Submitted / Not Submitted)
   - Submission Date and Time (if submitted)

### Submit Assignment
1. Click the "Submit" button for any assignment with "Not Submitted" status
2. Fill in the submission form:
   - Upload your assignment file
   - Add optional comments
3. Click "Submit Assignment"
4. Your assignment status will update immediately
5. You'll be redirected back to the home page

### Logout
1. Click "Logout" button in the navigation bar
2. You'll be redirected to the login page
3. Your session will be terminated

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| / | GET | Login page (redirect if logged in) |
| /login/ | GET, POST | User login |
| /home/ | GET | Dashboard with assignments (requires login) |
| /submit/<int:id>/ | GET, POST | Assignment submission (requires login) |
| /logout/ | GET | User logout |

## Security Features

1. **Session-Based Authentication**
   - Login information stored in browser session
   - Session expires after inactivity
   - Session token required to access pages

2. **Page Access Protection**
   - Decorator functions validate session on protected pages
   - Unauthorized users are redirected to login
   - Direct URL access is prevented

3. **Data Validation**
   - User credentials validated against database
   - Only assigned assignments can be accessed
   - Assignment submission properly validated

## Admin Panel

Access Django admin at: `http://127.0.0.1:8000/admin/`

### Default Admin Credentials
Create a superuser if needed:
```bash
py manage.py createsuperuser
```

Then log in with the credentials you create.

### Admin Features
- Create, read, update, delete users
- Manage assignments
- View submission history
- Filter and search users and assignments

## Customization

### Adding New Users
1. Access Django admin panel
2. Go to Users section
3. Click "Add User"
4. Enter username and password
5. Click "Save"

### Adding Assignments
1. Access Django admin panel
2. Go to Assignments section
3. Click "Add Assignment"
4. Select user, enter assignment name
5. Set initial status as "Not Submitted"
6. Click "Save"

## Troubleshooting

### Issue: "No such table: users"
**Solution**: Run migrations
```bash
py manage.py migrate
```

### Issue: Static files not loading
**Solution**: Collect static files
```bash
py manage.py collectstatic
```

### Issue: Login page not displaying
**Solution**: Ensure app is registered in INSTALLED_APPS
Check: `srspro/settings.py` - Should have `'srsapp'` in INSTALLED_APPS

### Issue: Session timeout too quick
**Solution**: Edit `srspro/settings.py` and adjust:
```python
SESSION_COOKIE_AGE = 3600  # Time in seconds
```

## File Descriptions

- **settings.py**: Django configuration, database setup, installed apps
- **urls.py**: URL routing configuration
- **views.py**: Business logic for login, home, submission
- **models.py**: Database table definitions
- **templates/**: HTML files for UI
- **static/**: CSS and JavaScript files
- **admin.py**: Django admin customization

## Features Documentation

### Login System
- Username and password validation
- Session storage for authenticated users
- Error messages for failed login attempts
- Responsive login form with Bootstrap styling

### Assignment List Page
- Displays all assignments for logged-in user
- Shows submission status with visual badges
- Displays submission date/time if available
- Action column with submit button for pending assignments

### Submission Page
- Clean form interface for file upload
- Optional comments field
- Loading animation during submission
- Confirmation message and redirect after successful submission

## Development Tips

1. **Debug Mode**: Already enabled in settings for development
2. **Database Reset**: Delete `db.sqlite3` and run migrations to reset
3. **View Database**: Access admin panel at `/admin/`
4. **Testing**: Login with test credentials provided above

## Performance Considerations

- SQLite is suitable for small to medium deployments
- Consider upgrading to PostgreSQL for production
- Static files are properly organized for caching
- Templates use efficient block inheritance

## Future Enhancements

- Email notifications for submissions
- Assignment deadline tracking
- Bulk upload capability
- Grade/feedback system
- Assignment history and analytics
- Password change functionality
- Two-factor authentication
- File size validation
- Supported file format checking

## Support & Maintenance

For any issues or questions:
1. Check the Troubleshooting section above
2. Review Django documentation: https://docs.djangoproject.com/
3. Check console for error messages
4. Verify database connectivity

## License

This project is created for educational purposes.

## Credits

Built with Django, Bootstrap, and jQuery for a complete student assignment submission system.

---

**Version**: 1.0  
**Last Updated**: February 2026  
**Django Version**: 6.0.2
