# Quick Start Guide - Reddit Persona Generator

## 🚀 Getting Started in 5 Minutes

### Step 1: Setup
Run the automated setup:
```bash
python setup.py
```

Or on Windows:
```bash
setup.bat
```

### Step 2: Add OpenAI API Key
Edit the `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your_actual_api_key_here
```

Get your API key from: https://platform.openai.com/api-keys

### Step 3: Run the Generator
```bash
python reddit_persona_generator.py https://www.reddit.com/user/kojied/
```

### Step 4: Check Results
Your persona will be saved in the `output/` directory as a `.txt` file.

## 📋 Sample Commands

Generate persona for the test users:
```bash
# User 1
python reddit_persona_generator.py https://www.reddit.com/user/kojied/

# User 2  
python reddit_persona_generator.py https://www.reddit.com/user/Hungry-Move-6603/
```

With custom options:
```bash
# Analyze fewer posts
python reddit_persona_generator.py https://www.reddit.com/user/kojied/ --max-posts 50

# Custom output directory
python reddit_persona_generator.py https://www.reddit.com/user/kojied/ --output-dir my_personas
```

## 🔧 Troubleshooting

**No OpenAI API Key Error:**
- Make sure you've added your API key to the `.env` file
- Check that your OpenAI account has sufficient credits

**Python not found:**
- Make sure Python 3.7+ is installed
- Check that Python is in your system PATH

**Permission errors:**
- Try running with administrator/sudo privileges
- Use `pip install --user` if needed

## 📁 Output Example

The generated persona file will look like this:
```
=============================================================
USER PERSONA: kojied
=============================================================

DEMOGRAPHICS:
• Age Range: 25-35
• Occupation: Software Developer

INTERESTS:
• Programming
• Gaming
• Technology

... (and much more)
```

## 🎯 Next Steps

1. Test with the provided sample users
2. Try with other Reddit users
3. Adjust the `--max-posts` parameter based on your needs
4. Review the generated personas for accuracy
5. Consider the ethical implications of persona generation

## 📚 Additional Resources

- Full documentation: `README.md`
- Test the installation: `python test_generator.py`
- View help: `python reddit_persona_generator.py --help`
- Example usage: `python example_usage.py`
