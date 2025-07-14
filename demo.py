#!/usr/bin/env python3
"""
Reddit Persona Generator - Demonstration Script
This script shows the capabilities of the Reddit Persona Generator
"""

import os
import sys
import time

def print_header(title):
    """Print a formatted header."""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def print_step(step_num, description):
    """Print a formatted step."""
    print(f"\n{step_num}. {description}")
    print("-" * 40)

def demo_url_validation():
    """Demonstrate URL validation."""
    from reddit_persona_generator import RedditScraper
    
    scraper = RedditScraper()
    
    test_urls = [
        ("https://www.reddit.com/user/kojied/", True),
        ("https://www.reddit.com/user/Hungry-Move-6603/", True),
        ("https://reddit.com/user/invalid/", False),
        ("https://www.reddit.com/r/programming/", False),
        ("invalid_url", False)
    ]
    
    print("Testing URL validation:")
    for url, expected in test_urls:
        result = scraper.validate_url(url)
        status = "✓" if result == expected else "✗"
        print(f"  {status} {url[:50]:<50} -> {'Valid' if result else 'Invalid'}")

def demo_persona_formatting():
    """Demonstrate persona formatting."""
    from reddit_persona_generator import PersonaFormatter, UserPersona
    
    sample_persona = UserPersona(
        name="DemoUser",
        age_range="25-35",
        occupation="Software Developer",
        interests=["Programming", "Gaming", "Technology"],
        personality_traits=["Analytical", "Helpful", "Detail-oriented"],
        values=["Quality", "Learning", "Community"],
        goals=["Improve skills", "Help others", "Build software"],
        pain_points=["Time management", "Keeping up with tech"],
        preferred_communication_style="Technical and helpful",
        activity_level="Regular contributor",
        technical_proficiency="Advanced",
        citations={
            "interests": ["https://reddit.com/post1", "https://reddit.com/post2"],
            "personality_traits": ["https://reddit.com/post3"]
        }
    )
    
    print("Sample persona format:")
    formatted = PersonaFormatter.format_persona(sample_persona)
    print(formatted[:500] + "..." if len(formatted) > 500 else formatted)

def demo_file_structure():
    """Show the project file structure."""
    print("Project structure:")
    files = [
        "reddit_persona_generator.py  # Main application",
        "setup.py                    # Automated setup",
        "test_generator.py           # Test suite",
        "requirements.txt            # Dependencies",
        "README.md                   # Documentation",
        "QUICKSTART.md              # Quick start guide",
        "output/                     # Generated personas",
        "  ├── kojied_persona.txt    # Sample output",
        "  └── Hungry-Move-6603_persona.txt",
        ".env.template               # Environment setup",
        ".github/                    # GitHub configuration",
        ".vscode/                    # VS Code tasks"
    ]
    
    for file in files:
        print(f"  {file}")

def demo_usage_examples():
    """Show usage examples."""
    print("Usage examples:")
    examples = [
        "python reddit_persona_generator.py https://www.reddit.com/user/kojied/",
        "python reddit_persona_generator.py https://www.reddit.com/user/Hungry-Move-6603/",
        "python reddit_persona_generator.py https://www.reddit.com/user/kojied/ --max-posts 50",
        "python reddit_persona_generator.py https://www.reddit.com/user/kojied/ --output-dir my_personas"
    ]
    
    for example in examples:
        print(f"  {example}")

def demo_features():
    """Demonstrate key features."""
    print("Key features:")
    features = [
        "✓ Reddit profile URL validation",
        "✓ Web scraping of posts and comments",
        "✓ LLM-powered persona generation",
        "✓ Comprehensive citation system",
        "✓ Professional text file output",
        "✓ PEP-8 compliant code",
        "✓ Type hints and documentation",
        "✓ Error handling and validation",
        "✓ Cross-platform compatibility",
        "✓ Automated setup and testing"
    ]
    
    for feature in features:
        print(f"  {feature}")

def main():
    """Main demonstration function."""
    print_header("Reddit Persona Generator - Demonstration")
    
    print("This script demonstrates the capabilities of the Reddit Persona Generator.")
    print("The tool analyzes Reddit user profiles to create detailed personas.")
    
    print_step(1, "Project Overview")
    demo_features()
    
    print_step(2, "File Structure")
    demo_file_structure()
    
    print_step(3, "URL Validation Demo")
    demo_url_validation()
    
    print_step(4, "Persona Format Demo")
    demo_persona_formatting()
    
    print_step(5, "Usage Examples")
    demo_usage_examples()
    
    print_header("Setup Instructions")
    print("1. Run: python setup.py")
    print("2. Add your OpenAI API key to .env file")
    print("3. Test: python test_generator.py")
    print("4. Use: python reddit_persona_generator.py <reddit_url>")
    
    print_header("Ready to Use!")
    print("The Reddit Persona Generator is fully configured and ready to use.")
    print("Check the sample output files in the output/ directory.")
    print("For detailed instructions, see README.md and QUICKSTART.md")
    
    if "--test" in sys.argv:
        print("\nRunning quick test...")
        try:
            from reddit_persona_generator import RedditScraper
            scraper = RedditScraper()
            test_url = "https://www.reddit.com/user/kojied/"
            username = scraper.extract_username(test_url)
            print(f"✓ Successfully extracted username: {username}")
        except Exception as e:
            print(f"✗ Test failed: {e}")

if __name__ == "__main__":
    main()
