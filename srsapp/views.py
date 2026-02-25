from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import User, Assignment
import hashlib
from functools import wraps

# Decorator to check if user is logged in
def login_required_decorator(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if 'username' not in request.session:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper


def login_view(request):
    """Handle user login"""
    error_message = None
    
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        try:
            user = User.objects.get(username=username)
            # Simple password check (in production, use proper hashing and salting)
            if user.password == password:
                # Store username in session
                request.session['username'] = username
                request.session.set_expiry(3600)  # Session expires in 1 hour
                return redirect('home')
            else:
                error_message = "Invalid username or password"
        except User.DoesNotExist:
            error_message = "Invalid username or password"
    
    context = {'error_message': error_message}
    return render(request, 'login.html', context)


@login_required_decorator
def home_view(request):
    """Display assignments for the logged-in user"""
    username = request.session.get('username')
    
    try:
        user = User.objects.get(username=username)
        assignments = Assignment.objects.filter(username=user)
        context = {
            'username': username,
            'assignments': assignments,
        }
        return render(request, 'home.html', context)
    except User.DoesNotExist:
        return redirect('login')


@login_required_decorator
def submit_assignment_view(request, assignment_id):
    """Handle assignment submission"""
    username = request.session.get('username')
    
    try:
        user = User.objects.get(username=username)
        assignment = get_object_or_404(Assignment, assignment_id=assignment_id, username=user)
        
        if request.method == 'POST':
            # Update assignment status
            assignment.submitted_status = 'Submitted'
            assignment.submitted_time = timezone.now()
            assignment.save()
            return redirect('home')
        
        context = {
            'username': username,
            'assignment': assignment,
        }
        return render(request, 'submit.html', context)
    except User.DoesNotExist:
        return redirect('login')


@login_required_decorator
def logout_view(request):
    """Handle user logout"""
    if 'username' in request.session:
        del request.session['username']
    request.session.flush()
    return redirect('login')
