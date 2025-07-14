#!/usr/bin/env python3
"""
Example usage of the Reddit Persona Generator
This script demonstrates how to use the generator programmatically
"""

import os
import sys
from reddit_persona_generator import RedditScraper, PersonaGenerator, PersonaFormatter

def example_usage():
    """Example of how to use the Reddit Persona Generator."""
    
    # Example Reddit user URLs
    example_urls = [
        "https://www.reddit.com/user/kojied/",
        "https://www.reddit.com/user/Hungry-Move-6603/"
    ]
    
    print("Reddit Persona Generator - Example Usage")
    print("=" * 50)
    
    # Check if OpenAI API key is set
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  OpenAI API key not found in environment variables")
        print("This example will show the structure but won't generate actual personas")
        print("To use with OpenAI, set the OPENAI_API_KEY environment variable")
        print()
    
    for url in example_urls:
        print(f"Processing: {url}")
        
        try:
            # Initialize scraper
            scraper = RedditScraper()
            username = scraper.extract_username(url)
            
            print(f"Username: {username}")
            print("Scraping Reddit content...")
            
            # In a real scenario, this would scrape actual content
            print("(This is a demo - actual scraping would happen here)")
            
            # Example of what the scraper would return
            sample_posts = []  # Would be populated by scraper.scrape_user_content(url)
            
            print(f"Found {len(sample_posts)} posts/comments")
            
            # If we had OpenAI API key, we would generate the persona
            if os.getenv('OPENAI_API_KEY'):
                persona_generator = PersonaGenerator()
                persona = persona_generator.generate_persona(sample_posts, username)
                
                # Save persona
                filepath = PersonaFormatter.save_persona(persona)
                print(f"✓ Persona saved to: {filepath}")
            else:
                print("✓ Persona would be generated and saved here")
            
            print()
            
        except Exception as e:
            print(f"❌ Error processing {url}: {e}")
            print()

def main():
    """Main function."""
    print("This script demonstrates how to use the Reddit Persona Generator")
    print("For actual usage, run: python reddit_persona_generator.py <reddit_url>")
    print()
    
    example_usage()
    
    print("For more information, see the README.md file")

if __name__ == "__main__":
    main()
