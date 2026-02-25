@echo off
REM Student Record Submission System - Startup Script
REM This script starts the Django development server

echo.
echo =========================================
echo Student Record Submission System
echo =========================================
echo.

REM Change to project directory
cd /d "%~dp0"

REM Check if manage.py exists
if not exist manage.py (
    echo Error: manage.py not found. Please run this script from the project root directory.
    pause
    exit /b 1
)

REM Welcome message
echo Starting Django development server...
echo.
echo The application will be available at:
echo   http://127.0.0.1:8000/
echo.
echo Test Credentials:
echo   Username: john_doe
echo   Password: password123
echo.
echo Press CTRL+C to stop the server.
echo =========================================
echo.

REM Run the development server
py manage.py runserver

REM Pause if there was an error
if errorlevel 1 (
    echo.
    echo An error occurred. Please check the output above.
    pause
)
