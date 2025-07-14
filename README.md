# Reddit User Persona Generator

A Python script that analyzes Reddit user profiles to generate comprehensive user personas based on their posts and comments. The tool uses web scraping and Large Language Models (LLMs) to extract meaningful insights about users' demographics, interests, personality traits, and behaviors.

## Features

- **Profile Analysis**: Scrapes Reddit user posts and comments
- **AI-Powered Insights**: Uses OpenAI's GPT models to analyze content
- **Comprehensive Personas**: Generates detailed user personas with demographics, interests, personality traits, values, goals, and pain points
- **Citation System**: Links each persona characteristic to specific posts/comments as evidence
- **Flexible Output**: Saves personas as formatted text files
- **PEP-8 Compliant**: Follows Python coding standards

## Prerequisites

- Python 3.7 or higher
- OpenAI API key (required for persona generation)
- Internet connection for Reddit scraping

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/reddit-persona-generator.git
   cd reddit-persona-generator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API key**:
   
   Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   
   Or set it as an environment variable:
   ```bash
   # Windows (PowerShell)
   $env:OPENAI_API_KEY="your_openai_api_key_here"
   
   # Windows (Command Prompt)
   set OPENAI_API_KEY=your_openai_api_key_here
   
   # Linux/Mac
   export OPENAI_API_KEY="your_openai_api_key_here"
   ```

## Usage

### Basic Usage

```bash
python reddit_persona_generator.py https://www.reddit.com/user/username/
```

### Advanced Usage

```bash
# Analyze with custom number of posts
python reddit_persona_generator.py https://www.reddit.com/user/username/ --max-posts 50

# Custom output directory
python reddit_persona_generator.py https://www.reddit.com/user/username/ --output-dir my_personas

# Full example with all options
python reddit_persona_generator.py https://www.reddit.com/user/kojied/ --max-posts 100 --output-dir output
```

### Command Line Options

- `url`: Reddit user profile URL (required)
- `--max-posts`: Maximum number of posts to analyze (default: 100)
- `--output-dir`: Output directory for persona files (default: output)

### Example URLs

The script works with standard Reddit user profile URLs:
- `https://www.reddit.com/user/kojied/`
- `https://www.reddit.com/user/Hungry-Move-6603/`

## Sample Output

The script generates a comprehensive user persona file that includes:

### Demographics
- Age range estimation
- Likely occupation or field of work

### Psychological Profile
- Interests and hobbies
- Personality traits
- Values and beliefs
- Goals and aspirations
- Pain points and challenges

### Communication & Activity
- Communication style
- Reddit activity level
- Technical proficiency

### Citations
- Links to specific posts/comments used to derive each characteristic
- Evidence-based persona generation

## Sample Personas

The repository includes sample persona files for the provided test users:

- `output/kojied_persona.txt`
- `output/Hungry-Move-6603_persona.txt`

## Technical Details

### Architecture

The script consists of four main components:

1. **RedditScraper**: Handles Reddit content extraction
2. **PersonaGenerator**: Uses OpenAI API for content analysis
3. **PersonaFormatter**: Formats and saves personas
4. **Main Controller**: Orchestrates the workflow

### Data Processing

1. **Content Extraction**: Scrapes posts and comments using Reddit's JSON API
2. **Content Analysis**: Processes text using OpenAI's GPT models
3. **Citation Matching**: Links persona characteristics to source content
4. **Output Generation**: Formats results as human-readable text files

### Error Handling

- Validates Reddit URLs
- Handles API rate limits
- Provides fallback personas if API fails
- Comprehensive error messages

## API Rate Limits

The script includes built-in rate limiting to respect Reddit's API guidelines:
- Delays between requests
- Maximum post limits
- Graceful error handling

## Privacy and Ethics

This tool is designed for research and educational purposes. Please ensure:
- Respect Reddit's Terms of Service
- Use responsibly and ethically
- Consider privacy implications
- Don't use for harassment or stalking

## Troubleshooting

### Common Issues

1. **OpenAI API Key Error**:
   - Ensure your API key is correctly set in the environment
   - Check that your OpenAI account has sufficient credits

2. **No Posts Found**:
   - User profile might be private or deleted
   - Check if the URL is correct
   - User might have no public posts

3. **Rate Limiting**:
   - Reddit might be temporarily blocking requests
   - Wait a few minutes and try again

4. **Installation Issues**:
   - Ensure Python 3.7+ is installed
   - Try using `pip3` instead of `pip`
   - Consider using a virtual environment

### Debug Mode

For troubleshooting, you can add debug prints or modify the script to output more detailed information about the scraping process.

## Development

### Code Structure

```
reddit_persona_generator.py
├── RedditScraper class
├── PersonaGenerator class  
├── PersonaFormatter class
├── Data classes (RedditPost, UserPersona)
└── Main function
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Follow PEP-8 guidelines
4. Add tests for new functionality
5. Submit a pull request

### Testing

To test the script with different users:

```bash
# Test with the provided sample users
python reddit_persona_generator.py https://www.reddit.com/user/kojied/
python reddit_persona_generator.py https://www.reddit.com/user/Hungry-Move-6603/
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the GPT API
- Reddit for the content API
- Python community for the excellent libraries

## Disclaimer

This tool is for educational and research purposes only. Always respect user privacy and platform terms of service. The generated personas are AI-generated interpretations and should not be considered as factual profiles of real individuals.
