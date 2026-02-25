#!/bin/bash
# Student Record Submission System - Startup Script
# This script starts the Django development server

echo ""
echo "========================================="
echo "Student Record Submission System"
echo "========================================="
echo ""

# Change to project directory
cd "$(dirname "$0")"

# Check if manage.py exists
if [ ! -f manage.py ]; then
    echo "Error: manage.py not found. Please run this script from the project root directory."
    exit 1
fi

# Welcome message
echo "Starting Django development server..."
echo ""
echo "The application will be available at:"
echo "  http://127.0.0.1:8000/"
echo ""
echo "Test Credentials:"
echo "  Username: john_doe"
echo "  Password: password123"
echo ""
echo "Press CTRL+C to stop the server."
echo "========================================="
echo ""

# Run the development server
python manage.py runserver

# Exit
echo ""
echo "Server stopped."
