# Reddit Persona Generator Setup Script for PowerShell
# Run this script to set up the environment

Write-Host "Reddit Persona Generator - Setup" -ForegroundColor Green
Write-Host "====================================" -ForegroundColor Green
Write-Host ""

# Check Python installation
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.7+ from https://python.org" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Run setup script
Write-Host "Running setup script..." -ForegroundColor Yellow
try {
    python setup.py
    Write-Host ""
    Write-Host "Setup complete! 🎉" -ForegroundColor Green
    Write-Host ""
    Write-Host "Usage examples:" -ForegroundColor Cyan
    Write-Host "python reddit_persona_generator.py https://www.reddit.com/user/kojied/" -ForegroundColor White
    Write-Host "python reddit_persona_generator.py https://www.reddit.com/user/Hungry-Move-6603/" -ForegroundColor White
    Write-Host ""
    Write-Host "Don't forget to add your OpenAI API key to the .env file!" -ForegroundColor Yellow
} catch {
    Write-Host "❌ Setup failed: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

Write-Host ""
Read-Host "Press Enter to exit"
