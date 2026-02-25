# Student Record Submission System - Testing Guide

## Test Scenarios

### Scenario 1: User Login
**Objective**: Test user authentication system

#### Test Steps:
1. Navigate to http://127.0.0.1:8000/
2. Try login with invalid credentials:
   - username: "invalid_user", password: "wrong_pass"
   - Expected: Error message appears
3. Login with valid username "john_doe", password "password123"
   - Expected: Redirect to home page, welcome message shows

#### Pass Criteria:
- ✓ Invalid login shows error message
- ✓ Valid login redirects to home page
- ✓ Session is created after login

---

### Scenario 2: Assignment List Display
**Objective**: Test assignment list and status display

#### Test Steps:
1. Login as john_doe
2. View home page with assignment list
3. Check that all 3 assignments are displayed:
   - "Python Project" - Not Submitted (yellow badge)
   - "Django REST API" - Submitted (green badge)
   - "Database Design" - Not Submitted (yellow badge)
4. Verify submission dates show correctly

#### Pass Criteria:
- ✓ All assignments display correctly
- ✓ Status badges show correct color (yellow/green)
- ✓ Submitted assignments show date/time
- ✓ Not submitted assignments show submit button

---

### Scenario 3: Assignment Submission
**Objective**: Test assignment submission functionality

#### Test Steps:
1. Login as jane_smith (password: pass456)
2. View home page - should have "Web Development" not submitted
3. Click Submit button on "Web Development"
4. Fill submission form:
   - Upload any file (or test without file)
   - Add optional comment like "This is my submission"
5. Click "Submit Assignment"
6. Check if status updates to "Submitted"
7. Verify redirect back to home page
8. Confirm assignment status changed

#### Pass Criteria:
- ✓ Submit page loads correctly
- ✓ Can fill and submit form
- ✓ Status updates from "Not Submitted" to "Submitted"
- ✓ Timestamp is recorded
- ✓ Redirect to home page after submission

---

### Scenario 4: Session Management
**Objective**: Test session-based access control

#### Test Steps:
1. Login with valid credentials
2. Try accessing /home/ directly - should work
3. Try accessing /submit/1/ directly - should work (if logged in)
4. Click Logout
5. Try accessing /home/ directly
6. Expected: Redirect to login page
7. Try accessing /submit/1/ directly
8. Expected: Redirect to login page

#### Pass Criteria:
- ✓ Protected pages require login
- ✓ Session is cleared on logout
- ✓ Cannot access protected pages without session
- ✓ Direct URL access to protected pages redirects to login

---

### Scenario 5: Multiple Users
**Objective**: Test user isolation

#### Test Steps:
1. Login as alice_jones (password: alice789)
2. View assignments - should see only alice's assignments:
   - "HTML & CSS" - Not Submitted
   - "Vue.js Framework" - Not Submitted
3. Should NOT see john_doe's or jane_smith's assignments
4. Logout and login as john_doe
5. Verify john_doe sees only his assignments

#### Pass Criteria:
- ✓ Users only see their own assignments
- ✓ Each user has isolated data
- ✓ No data cross-contamination between users

---

### Scenario 6: Browser History & Back Button
**Objective**: Test session expiry and history navigation

#### Test Steps:
1. Login successfully
2. Skip through pages (home > submit > home)
3. Click browser back button
4. Verify appropriate pages load
5. Wait for session timeout (default 1 hour)
6. Try clicking back button - may redirect to login

#### Pass Criteria:
- ✓ Navigation works smoothly
- ✓ Back button functions correctly
- ✓ Session timeout redirects to login

---

### Scenario 7: Admin Panel
**Objective**: Test Django admin functionality

#### Test Steps:
1. Navigate to http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. View Users section
4. View Assignments section
5. Create new user:
   - username: "test_user", password: "test123"
6. Create assignment for the new user
7. Logout from admin
8. Login as new test_user in main application

#### Pass Criteria:
- ✓ Admin panel loads
- ✓ Can view users and assignments
- ✓ Can create new users
- ✓ Can create new assignments
- ✓ Can filter and search
- ✓ New user can login to main app

---

### Scenario 8: Responsive Design
**Objective**: Test mobile/responsive layout

#### Test Steps:
1. Open app in desktop browser
2. Check all pages display correctly
3. Resize browser window to simulate mobile (375px width)
4. Test on mobile device if available
5. Verify:
   - Navigation bar adapts
   - Tables stack on mobile
   - Buttons are clickable
   - Forms are readable

#### Pass Criteria:
- ✓ Desktop layout works well
- ✓ Tablet layout is responsive
- ✓ Mobile layout is usable
- ✓ All elements are accessible on small screens

---

### Scenario 9: Error Handling
**Objective**: Test error messages and handling

#### Test Steps:
1. Try accessing non-existent assignment:
   - URL: /submit/99999/
   - Expected: 404 error or appropriate message
2. Try submitting without upload:
   - Note: Current implementation doesn't require file
   - Verify submission completes
3. Check browser console for JavaScript errors
4. Try rapid multiple submissions
5. Expected: Should prevent double submission

#### Pass Criteria:
- ✓ Appropriate error messages display
- ✓ No JavaScript errors in console
- ✓ Graceful error handling
- ✓ Double submission prevention works

---

### Scenario 10: UI/UX Quality
**Objective**: Test user interface quality

#### Test Steps:
1. Check all pages for:
   - Proper Bootstrap styling
   - Consistent colors and fonts
   - Proper spacing and alignment
2. Test all interactive elements:
   - Hover effects on buttons
   - Links work correctly
   - Form inputs respond to user input
3. Check animations:
   - Page load animations
   - Button hover effects
   - Loading spinners appear/disappear correctly

#### Pass Criteria:
- ✓ Clean, professional appearance
- ✓ Consistent design across pages
- ✓ All interactive elements respond correctly
- ✓ Animations are smooth and appropriate

---

## Integration Tests

### Test 1: Complete User Flow
```
1. Navigate to application
2. Login as new test user
3. View assignments
4. Submit one assignment
5. Verify status changed
6. Logout
7. Login again as same user
8. Verify previous submission persists
```

### Test 2: Multiple User Concurrent Access
```
1. Open two browser windows
2. Login as different users in each
3. View different assignments in each window
4. Submit assignment in window 1
5. Verify it doesn't affect user 2's view
6. Logout both
7. Verify both redirected to login
```

### Test 3: Admin Data Management
```
1. Admin creates new user
2. Admin creates assignments for new user
3. New user logs in
4. Verifies assignments are visible
5. Submits assignment
6. Admin views submitted assignment
7. Admin can see submission timestamp
```

---

## Performance Tests

### Load Test
```bash
# Using Apache Bench (if available)
ab -n 100 -c 10 http://127.0.0.1:8000/login/
```

### Database Query Optimization
```bash
# In Django shell:
from django.db import connection
from django.test.utils import CaptureQueriesContext

with CaptureQueriesContext(connection) as context:
    # Run query
    list(Assignment.objects.filter(username__username='john_doe'))

print(f"Queries executed: {len(context)}")
for q in context:
    print(q['sql'])
```

---

## Security Tests

### Test 1: SQL Injection
```
Username: ' OR '1'='1
Password: anything
Expected: No login, error message displayed
```

### Test 2: Session Hijacking Prevention
```
1. Login successfully
2. Try modifying session ID in browser cookies
3. Expected: Session invalidated or redirected
```

### Test 3: Direct URL Access
```
1. Without login, try visiting:
   - /home/
   - /submit/1/
2. Expected: Redirect to login page
```

### Test 4: CSRF Protection
```
1. Login to application
2. Check page source for CSRF token in forms
3. Expected: All forms have {% csrf_token %}
```

---

## Test Data Cleanup

### Reset Database
```bash
py manage.py flush
py manage.py populate_test_data
```

### Clear Sessions
```bash
py manage.py clearsessions
```

### Delete Specific User
```bash
py manage.py shell
from srsapp.models import User
User.objects.filter(username='test_user').delete()
```

---

## Test Checklist

- [ ] Login with correct credentials works
- [ ] Login with incorrect credentials shows error
- [ ] Assignments list displays correctly
- [ ] Status badges show correct colors
- [ ] Submit button appears only for unsubmitted assignments
- [ ] Submission form accepts input
- [ ] Status updates after submission
- [ ] Timestamp records correctly
- [ ] User sees only own assignments
- [ ] Protected pages redirect to login if not authenticated
- [ ] Logout clears session
- [ ] Back button works correctly
- [ ] Mobile responsive
- [ ] No JavaScript errors
- [ ] Admin panel works
- [ ] New users can be created
- [ ] New assignments can be created
- [ ] Database is uncorrupted
- [ ] All links work
- [ ] All forms submit correctly

---

## Known Issues & Workarounds

### Issue: Session expires during testing
**Workaround**: Edit settings.py SESSION_COOKIE_AGE to a longer duration

### Issue: Static files not loading in development
**Workaround**: Ensure DEBUG=True and run collectstatic

### Issue: Multiple users cant login simultaneously (single test)
**Workaround**: Use different browsers or incognito windows

---

## Automated Testing (Future Enhancement)

```python
# Example: tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from srsapp.models import Assignment

class LoginTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='john', password='pass123')
    
    def test_valid_login(self):
        response = self.client.post('/login/', {
            'username': 'john',
            'password': 'pass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertIn('username', self.client.session)
```

Run tests with: `py manage.py test`

---

**Test Date**: [current date]  
**Tested By**: [your name]  
**Status**: [Pass/Fail]  
**Notes**: [any additional notes]
