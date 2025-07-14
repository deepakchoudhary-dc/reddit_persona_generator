#!/usr/bin/env python3
"""
Setup script for Reddit Persona Generator
Helps users set up the environment and dependencies
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    else:
        print(f"✓ Python {sys.version} is compatible")

def install_dependencies():
    """Install required dependencies."""
    print("Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        sys.exit(1)

def create_env_file():
    """Create .env file if it doesn't exist."""
    if not os.path.exists('.env'):
        print("Creating .env file...")
        with open('.env', 'w') as f:
            f.write("# OpenAI API Key\n")
            f.write("# Get your API key from: https://platform.openai.com/api-keys\n")
            f.write("OPENAI_API_KEY=your_openai_api_key_here\n")
        print("✓ .env file created")
        print("📝 Please edit .env file and add your OpenAI API key")
    else:
        print("✓ .env file already exists")

def create_output_directory():
    """Create output directory if it doesn't exist."""
    if not os.path.exists('output'):
        os.makedirs('output')
        print("✓ Output directory created")
    else:
        print("✓ Output directory already exists")

def run_tests():
    """Run basic tests."""
    print("Running tests...")
    try:
        subprocess.check_call([sys.executable, "test_generator.py"])
    except subprocess.CalledProcessError as e:
        print(f"❌ Tests failed: {e}")
        return False
    return True

def show_usage_examples():
    """Show usage examples."""
    print("\n" + "="*60)
    print("SETUP COMPLETE! 🎉")
    print("="*60)
    print("\nNext steps:")
    print("1. Edit the .env file and add your OpenAI API key")
    print("2. Run the script with a Reddit user URL")
    print("\nUsage examples:")
    print("python reddit_persona_generator.py https://www.reddit.com/user/kojied/")
    print("python reddit_persona_generator.py https://www.reddit.com/user/Hungry-Move-6603/")
    print("\nFor more options:")
    print("python reddit_persona_generator.py --help")
    print("\nOutput files will be saved in the 'output' directory")
    print("="*60)

def main():
    """Main setup function."""
    print("Reddit Persona Generator Setup")
    print("="*40)
    
    # Check Python version
    check_python_version()
    
    # Install dependencies
    install_dependencies()
    
    # Create necessary files and directories
    create_env_file()
    create_output_directory()
    
    # Run tests
    if run_tests():
        show_usage_examples()
    else:
        print("\n⚠️  Setup completed but tests failed")
        print("The script should still work, but please check for issues")

if __name__ == "__main__":
    main()
