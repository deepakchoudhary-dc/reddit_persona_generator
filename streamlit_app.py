import streamlit as st
import os
from reddit_persona_generator import RedditScraper, PersonaGenerator, PersonaFormatter
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Reddit User Persona Generator", layout="centered")
st.title("🤖 Reddit User Persona Generator")
st.write("""
Enter a Reddit user profile URL (e.g., `https://www.reddit.com/user/username/`) to generate a detailed persona using LLM analysis. No data is stored or shared. Your API key is loaded from your `.env` file for privacy.
""")

url = st.text_input("Reddit User Profile URL", "https://www.reddit.com/user/")
max_posts = st.slider("Max posts/comments to analyze", 10, 200, 50, step=10)
run_button = st.button("Generate Persona")

if run_button and url.strip().startswith("https://www.reddit.com/user/"):
    with st.spinner("Scraping Reddit and generating persona..."):
        try:
            scraper = RedditScraper()
            username = scraper.extract_username(url)
            posts = scraper.scrape_user_content(url, max_posts)
            if not posts:
                st.error("No posts/comments found or scraping failed.")
            else:
                persona_generator = PersonaGenerator()
                persona = persona_generator.generate_persona(posts, username)
                persona_text = PersonaFormatter.format_persona(persona)
                st.success(f"Persona generated for user: {username}")
                st.code(persona_text, language="markdown")
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.markdown("""
*This tool uses OpenRouter for LLM inference. No API keys or user data are stored. All processing is local and privacy-respecting.*
""")
