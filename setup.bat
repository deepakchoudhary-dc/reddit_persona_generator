@echo off
echo Reddit Persona Generator - Quick Setup
echo ========================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

echo Running setup script...
python setup.py

echo.
echo Setup complete! You can now run:
echo python reddit_persona_generator.py https://www.reddit.com/user/username/
echo.
pause
