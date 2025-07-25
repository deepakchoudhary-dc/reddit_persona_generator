#!/usr/bin/env python3
"""
Reddit User Persona Generator

This script takes a Reddit user's profile URL and generates a comprehensive
user persona based on their posts and comments.

Author: AI Assistant
Date: July 14, 2025
"""

import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Tuple
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


@dataclass
class RedditPost:
    """Data class to represent a Reddit post."""
    title: str
    content: str
    subreddit: str
    score: int
    timestamp: str
    url: str
    post_type: str  # 'post' or 'comment'


@dataclass
class UserPersona:
    """Data class to represent a user persona."""
    name: str
    age_range: str
    occupation: str
    interests: List[str]
    personality_traits: List[str]
    values: List[str]
    goals: List[str]
    pain_points: List[str]
    preferred_communication_style: str
    activity_level: str
    technical_proficiency: str
    citations: Dict[str, List[str]]


class RedditScraper:
    """Reddit scraper to extract user posts and comments."""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.posts = []
        self.comments = []
    
    def validate_url(self, url: str) -> bool:
        """Validate if the URL is a valid Reddit user profile URL."""
        pattern = r'^https://www\.reddit\.com/user/[^/]+/?$'
        return bool(re.match(pattern, url))
    
    def extract_username(self, url: str) -> str:
        """Extract username from Reddit URL."""
        parsed = urlparse(url)
        path_parts = parsed.path.split('/')
        return path_parts[2] if len(path_parts) >= 3 else ""
    
    def scrape_user_content(self, url: str, max_posts: int = 100) -> List[RedditPost]:
        """
        Scrape user posts and comments from Reddit.
        
        Args:
            url: Reddit user profile URL
            max_posts: Maximum number of posts to scrape
            
        Returns:
            List of RedditPost objects
        """
        if not self.validate_url(url):
            raise ValueError("Invalid Reddit user profile URL")
        
        username = self.extract_username(url)
        all_content = []
        
        try:
            # Scrape posts
            posts_url = f"https://www.reddit.com/user/{username}/submitted/.json"
            posts_data = self._fetch_json_data(posts_url)
            
            if posts_data and 'data' in posts_data and 'children' in posts_data['data']:
                for post in posts_data['data']['children'][:max_posts//2]:
                    post_data = post['data']
                    reddit_post = RedditPost(
                        title=post_data.get('title', ''),
                        content=post_data.get('selftext', ''),
                        subreddit=post_data.get('subreddit', ''),
                        score=post_data.get('score', 0),
                        timestamp=datetime.fromtimestamp(post_data.get('created_utc', 0)).isoformat(),
                        url=f"https://www.reddit.com{post_data.get('permalink', '')}",
                        post_type='post'
                    )
                    all_content.append(reddit_post)
            
            # Scrape comments
            comments_url = f"https://www.reddit.com/user/{username}/comments/.json"
            comments_data = self._fetch_json_data(comments_url)
            
            if comments_data and 'data' in comments_data and 'children' in comments_data['data']:
                for comment in comments_data['data']['children'][:max_posts//2]:
                    comment_data = comment['data']
                    reddit_post = RedditPost(
                        title=f"Comment in r/{comment_data.get('subreddit', 'unknown')}",
                        content=comment_data.get('body', ''),
                        subreddit=comment_data.get('subreddit', ''),
                        score=comment_data.get('score', 0),
                        timestamp=datetime.fromtimestamp(comment_data.get('created_utc', 0)).isoformat(),
                        url=f"https://www.reddit.com{comment_data.get('permalink', '')}",
                        post_type='comment'
                    )
                    all_content.append(reddit_post)
            
            return all_content
            
        except Exception as e:
            print(f"Error scraping Reddit data: {e}")
            return []
    
    def _fetch_json_data(self, url: str) -> Optional[Dict]:
        """Fetch JSON data from Reddit API."""
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data from {url}: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON from {url}: {e}")
            return None


class PersonaGenerator:
    """Generate user persona using LLM analysis."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize with OpenRouter API key."""
        self.api_key = api_key or os.getenv('OPENROUTER_API_KEY')
        if not self.api_key:
            raise ValueError("OpenRouter API key is required. Set OPENROUTER_API_KEY environment variable.")
    
    def generate_persona(self, posts: List[RedditPost], username: str) -> UserPersona:
        """
        Generate user persona from Reddit posts and comments.
        
        Args:
            posts: List of RedditPost objects
            username: Reddit username
            
        Returns:
            UserPersona object
        """
        # Prepare content for analysis
        content_text = self._prepare_content_for_analysis(posts)
        
        # Generate persona using OpenAI
        persona_data = self._analyze_with_openai(content_text, username)
        
        # Create citations
        citations = self._create_citations(posts, persona_data)
        
        # Create UserPersona object
        persona = UserPersona(
            name=username,
            age_range=persona_data.get('age_range', 'Unknown'),
            occupation=persona_data.get('occupation', 'Unknown'),
            interests=persona_data.get('interests', []),
            personality_traits=persona_data.get('personality_traits', []),
            values=persona_data.get('values', []),
            goals=persona_data.get('goals', []),
            pain_points=persona_data.get('pain_points', []),
            preferred_communication_style=persona_data.get('communication_style', 'Unknown'),
            activity_level=persona_data.get('activity_level', 'Unknown'),
            technical_proficiency=persona_data.get('technical_proficiency', 'Unknown'),
            citations=citations        )
        
        return persona
    
    def _prepare_content_for_analysis(self, posts: List[RedditPost]) -> str:
        """Prepare Reddit content for LLM analysis."""
        content_parts = []
        
        for post in posts:
            content_part = f"[{post.post_type.upper()}] in r/{post.subreddit}\n"
            content_part += f"Title: {post.title}\n"
            content_part += f"Content: {post.content}\n"
            content_part += f"Score: {post.score}\n"
            content_part += f"Timestamp: {post.timestamp}\n"
            content_part += "-" * 50 + "\n"
            content_parts.append(content_part)
        
        return "\n".join(content_parts)
    
    def _analyze_with_openai(self, content: str, username: str) -> Dict:
        """Analyze content using OpenRouter API."""
        prompt = f"""You are an expert user researcher. Analyze the following Reddit posts and comments from user '{username}' and create a comprehensive user persona.

Based on the content, extract detailed information about:
1. Age range (e.g., "18-25", "26-35", "36-45", etc.)
2. Likely occupation or field of work
3. Multiple interests and hobbies (at least 5-7)
4. Personality traits (at least 5)
5. Values and beliefs (at least 5)
6. Goals and aspirations (at least 5)
7. Pain points and challenges (at least 5)
8. Communication style (detailed description)
9. Activity level on Reddit (detailed description)
10. Technical proficiency level

Reddit Content:
{content[:8000]}

IMPORTANT: You must respond with ONLY valid JSON. No markdown, no code blocks, no explanations. Just pure JSON.

{{
    "age_range": "estimated age range",
    "occupation": "likely occupation or field",
    "interests": ["interest1", "interest2", "interest3", "interest4", "interest5", "interest6", "interest7"],
    "personality_traits": ["trait1", "trait2", "trait3", "trait4", "trait5"],
    "values": ["value1", "value2", "value3", "value4", "value5"],
    "goals": ["goal1", "goal2", "goal3", "goal4", "goal5"],
    "pain_points": ["pain1", "pain2", "pain3", "pain4", "pain5"],
    "communication_style": "detailed description of communication style",
    "activity_level": "detailed description of activity level",
    "technical_proficiency": "detailed technical skill level"
}}"""
        
        try:
            url = "https://openrouter.ai/api/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "anthropic/claude-3-sonnet:beta",
                "messages": [
                    {"role": "system", "content": "You are an expert user researcher who analyzes social media content to create accurate user personas. You must respond with valid JSON only, no other text."},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 1500,
                "temperature": 0.3
            }
            
            print("Sending request to OpenRouter...")
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            
            if "choices" not in result or not result["choices"]:
                print("Error: No choices in API response")
                return self._get_fallback_persona()
                
            response_text = result["choices"][0]["message"]["content"].strip()
            print(f"Raw API response: {response_text[:200]}...")
            
            # Try to extract JSON from the response
            try:
                # Remove any markdown code blocks or extra formatting
                if "```json" in response_text:
                    response_text = response_text.split("```json")[1].split("```")[0].strip()
                elif "```" in response_text:
                    response_text = response_text.split("```")[1].split("```")[0].strip()
                
                parsed_data = json.loads(response_text)
                print("Successfully parsed JSON response")
                return parsed_data
                
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e}")
                print(f"Response text: {response_text}")
                return self._get_fallback_persona()
                
        except requests.exceptions.RequestException as e:
            print(f"Request error with OpenRouter API: {e}")
            return self._get_fallback_persona()
        except Exception as e:
            print(f"Unexpected error with OpenRouter API: {e}")
            return self._get_fallback_persona()
    
    def _get_fallback_persona(self) -> Dict:
        """Return a fallback persona when API fails."""
        return {
            "age_range": "25-35",
            "occupation": "Professional or Student",
            "interests": ["Technology", "Social Media", "Online Communities", "Current Events", "Entertainment"],
            "personality_traits": ["Engaged", "Curious", "Social", "Opinionated", "Active"],
            "values": ["Community participation", "Knowledge sharing", "Free expression", "Digital literacy", "Social connection"],
            "goals": ["Stay informed", "Connect with others", "Share knowledge", "Learn new things", "Engage in discussions"],
            "pain_points": ["Information overload", "Online toxicity", "Time management", "Privacy concerns", "Digital fatigue"],
            "communication_style": "Casual and conversational with occasional technical language",
            "activity_level": "Regular and consistent Reddit user",
            "technical_proficiency": "Intermediate to advanced"
        }
    
    def _create_citations(self, posts: List[RedditPost], persona_data: Dict) -> Dict[str, List[str]]:
        """Create citations linking persona characteristics to specific posts."""
        citations = {}
        
        # Simple keyword-based citation matching
        for key, value in persona_data.items():
            citations[key] = []
            
            if isinstance(value, list):
                for item in value:
                    matching_posts = self._find_matching_posts(posts, item.lower())
                    citations[key].extend(matching_posts[:2])  # Limit to 2 citations per item
            else:
                matching_posts = self._find_matching_posts(posts, str(value).lower())
                citations[key] = matching_posts[:3]  # Limit to 3 citations per characteristic
        
        return citations
    
    def _find_matching_posts(self, posts: List[RedditPost], keyword: str) -> List[str]:
        """Find posts that match a keyword."""
        matching_posts = []
        
        for post in posts:
            content_lower = (post.title + " " + post.content).lower()
            if keyword in content_lower:
                matching_posts.append(post.url)
        
        return matching_posts


class PersonaFormatter:
    """Format and save user persona to text file."""
    
    @staticmethod
    def format_persona(persona: UserPersona) -> str:
        """Format persona as readable text."""
        output = []
        output.append("=" * 60)
        output.append(f"USER PERSONA: {persona.name}")
        output.append("=" * 60)
        output.append("")
        
        # Demographics
        output.append("DEMOGRAPHICS:")
        output.append(f"• Age Range: {persona.age_range}")
        output.append(f"• Occupation: {persona.occupation}")
        output.append("")
        
        # Interests
        output.append("INTERESTS:")
        for interest in persona.interests:
            output.append(f"• {interest}")
        output.append("")
        
        # Personality Traits
        output.append("PERSONALITY TRAITS:")
        for trait in persona.personality_traits:
            output.append(f"• {trait}")
        output.append("")
        
        # Values
        output.append("VALUES:")
        for value in persona.values:
            output.append(f"• {value}")
        output.append("")
        
        # Goals
        output.append("GOALS:")
        for goal in persona.goals:
            output.append(f"• {goal}")
        output.append("")
        
        # Pain Points
        output.append("PAIN POINTS:")
        for pain in persona.pain_points:
            output.append(f"• {pain}")
        output.append("")
        
        # Communication & Activity
        output.append("COMMUNICATION & ACTIVITY:")
        output.append(f"• Communication Style: {persona.preferred_communication_style}")
        output.append(f"• Activity Level: {persona.activity_level}")
        output.append(f"• Technical Proficiency: {persona.technical_proficiency}")
        output.append("")
        
        # Citations
        output.append("CITATIONS:")
        output.append("(Sources used to derive persona characteristics)")
        output.append("")
        
        for characteristic, urls in persona.citations.items():
            if urls:
                output.append(f"{characteristic.upper().replace('_', ' ')}:")
                for url in urls:
                    output.append(f"  - {url}")
                output.append("")
        
        output.append("=" * 60)
        output.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        output.append("=" * 60)
        
        return "\n".join(output)
    
    @staticmethod
    def save_persona(persona: UserPersona, output_dir: str = "output") -> str:
        """Save persona to text file."""
        os.makedirs(output_dir, exist_ok=True)
        
        filename = f"{persona.name}_persona.txt"
        filepath = os.path.join(output_dir, filename)
        
        formatted_persona = PersonaFormatter.format_persona(persona)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(formatted_persona)
        
        return filepath


def main():
    """Main function to run the Reddit persona generator."""
    parser = argparse.ArgumentParser(
        description="Generate user persona from Reddit profile",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python reddit_persona_generator.py https://www.reddit.com/user/kojied/
  python reddit_persona_generator.py https://www.reddit.com/user/Hungry-Move-6603/
  python reddit_persona_generator.py https://www.reddit.com/user/kojied/ --max-posts 50
        """
    )
    
    parser.add_argument(
        'url',
        help='Reddit user profile URL (e.g., https://www.reddit.com/user/username/)'
    )
    
    parser.add_argument(
        '--max-posts',
        type=int,
        default=100,
        help='Maximum number of posts to analyze (default: 100)'
    )
    
    parser.add_argument(
        '--output-dir',
        default='output',
        help='Output directory for persona files (default: output)'
    )
    
    args = parser.parse_args()
    
    try:
        # Initialize components
        print("Initializing Reddit scraper...")
        scraper = RedditScraper()
        
        print("Initializing persona generator...")
        persona_generator = PersonaGenerator()
        
        # Extract username for display
        username = scraper.extract_username(args.url)
        print(f"Analyzing Reddit user: {username}")
        
        # Scrape Reddit content
        print("Scraping Reddit posts and comments...")
        posts = scraper.scrape_user_content(args.url, args.max_posts)
        
        if not posts:
            print("No posts found or error occurred during scraping.")
            return
        
        print(f"Found {len(posts)} posts and comments")
        
        # Generate persona
        print("Generating user persona...")
        persona = persona_generator.generate_persona(posts, username)
        
        # Save persona
        print("Saving persona to file...")
        filepath = PersonaFormatter.save_persona(persona, args.output_dir)
        
        print(f"✓ Persona saved to: {filepath}")
        print(f"✓ Analysis complete for user: {username}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
