# Estimate Token Count

A basic Python script that uses the Anthropic API to estimate the number of tokens in a message before sending it. The API returns the token count without invoking the model, making it useful for understanding token usage and managing costs when working with Claude models.

## Prerequisites

- Python 3.8+
- An [Anthropic API key](https://console.anthropic.com/)
- The `anthropic` Python package

Install the required package:

```bash
pip install anthropic
```

Set your API key as an environment variable:

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

## Run the Sample

```bash
python chat.py
```

The script will print a JSON response containing the token count for the provided system prompt and user message.

## Issues & Questions

If you run into any problems or have questions, please [file an issue](../../issues).
