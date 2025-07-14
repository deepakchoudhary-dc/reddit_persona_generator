#!/usr/bin/env python3
"""
Test script for Reddit Persona Generator
Tests the basic functionality without requiring OpenAI API
"""

import os
import sys
import tempfile
from reddit_persona_generator import RedditScraper, PersonaFormatter, UserPersona, RedditPost

def test_reddit_scraper():
    """Test Reddit scraper functionality."""
    print("Testing Reddit scraper...")
    
    scraper = RedditScraper()
    
    # Test URL validation
    valid_urls = [
        "https://www.reddit.com/user/kojied/",
        "https://www.reddit.com/user/Hungry-Move-6603/",
        "https://www.reddit.com/user/test_user/"
    ]
    
    invalid_urls = [
        "https://reddit.com/user/test/",
        "https://www.reddit.com/r/test/",
        "invalid_url",
        "https://www.reddit.com/user/test/posts/"
    ]
    
    for url in valid_urls:
        assert scraper.validate_url(url), f"Valid URL failed: {url}"
    
    for url in invalid_urls:
        assert not scraper.validate_url(url), f"Invalid URL passed: {url}"
    
    # Test username extraction
    test_cases = [
        ("https://www.reddit.com/user/kojied/", "kojied"),
        ("https://www.reddit.com/user/Hungry-Move-6603/", "Hungry-Move-6603"),
        ("https://www.reddit.com/user/test_user/", "test_user")
    ]
    
    for url, expected in test_cases:
        username = scraper.extract_username(url)
        assert username == expected, f"Username extraction failed: {url} -> {username} != {expected}"
    
    print("✓ Reddit scraper tests passed")

def test_persona_formatter():
    """Test persona formatter functionality."""
    print("Testing persona formatter...")
    
    # Create sample persona
    sample_persona = UserPersona(
        name="test_user",
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
            "personality_traits": ["https://reddit.com/post3"],
            "values": ["https://reddit.com/post4", "https://reddit.com/post5"]
        }
    )
    
    # Test formatting
    formatted = PersonaFormatter.format_persona(sample_persona)
    
    # Check if key sections are present
    assert "USER PERSONA: test_user" in formatted
    assert "DEMOGRAPHICS:" in formatted
    assert "INTERESTS:" in formatted
    assert "PERSONALITY TRAITS:" in formatted
    assert "VALUES:" in formatted
    assert "GOALS:" in formatted
    assert "PAIN POINTS:" in formatted
    assert "COMMUNICATION & ACTIVITY:" in formatted
    assert "CITATIONS:" in formatted
    
    # Test saving to file
    with tempfile.TemporaryDirectory() as temp_dir:
        filepath = PersonaFormatter.save_persona(sample_persona, temp_dir)
        assert os.path.exists(filepath)
        
        # Read back and verify
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            assert "test_user" in content
            assert "Software Developer" in content
    
    print("✓ Persona formatter tests passed")

def test_data_classes():
    """Test data classes."""
    print("Testing data classes...")
    
    # Test RedditPost
    post = RedditPost(
        title="Test Post",
        content="Test content",
        subreddit="test",
        score=10,
        timestamp="2025-07-14T15:30:00",
        url="https://reddit.com/post/test",
        post_type="post"
    )
    
    assert post.title == "Test Post"
    assert post.post_type == "post"
    
    # Test UserPersona
    persona = UserPersona(
        name="test_user",
        age_range="25-35",
        occupation="Developer",
        interests=["coding"],
        personality_traits=["helpful"],
        values=["quality"],
        goals=["improve"],
        pain_points=["time"],
        preferred_communication_style="casual",
        activity_level="moderate",
        technical_proficiency="intermediate",
        citations={}
    )
    
    assert persona.name == "test_user"
    assert len(persona.interests) == 1
    
    print("✓ Data classes tests passed")

def main():
    """Run all tests."""
    print("Running Reddit Persona Generator tests...")
    print("=" * 50)
    
    try:
        test_data_classes()
        test_reddit_scraper()
        test_persona_formatter()
        
        print("=" * 50)
        print("✓ All tests passed!")
        print("The Reddit Persona Generator is ready to use.")
        print("\nTo generate a persona, run:")
        print("python reddit_persona_generator.py https://www.reddit.com/user/username/")
        print("\nNote: You'll need to set up your OpenAI API key in the .env file")
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
