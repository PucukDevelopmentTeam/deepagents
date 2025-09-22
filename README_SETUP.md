# Research Agent Setup

## Prerequisites

1. **Get a Tavily API Key**:
   - Go to [Tavily](https://tavily.com/) and sign up for an account
   - Get your API key from the dashboard

2. **Get an Anthropic API Key** (for Claude):
   - Go to [Anthropic Console](https://console.anthropic.com/)
   - Create an account and get your API key

## Setup Steps

1. **Install dependencies** (already done):
   ```bash
   pip install deepagents tavily-python
   ```

2. **Set up environment variables**:
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env and add your actual API keys
   ```

3. **Run the example**:
   ```bash
   python research_example.py
   ```

## Environment Variables

Make sure to set these in your `.env` file or environment:

- `TAVILY_API_KEY`: Your Tavily API key for web search
- `ANTHROPIC_API_KEY`: Your Anthropic API key for Claude

## Example Usage

The script will research "what is langgraph?" and provide a comprehensive report.

You can modify the query in `research_example.py` to research any topic you're interested in.