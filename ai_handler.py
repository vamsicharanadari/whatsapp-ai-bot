# ai_handler.py
from openai import OpenAI
from config import YOUR_OPENAI_API_KEY

client = OpenAI(api_key=YOUR_OPENAI_API_KEY)

def parse_user_message(message: str):
    """
    Send user message to GPT and get structured response.
    Example response: {"action": "create_event", "title": "Meeting", "date": "2025-07-29", "time": "17:00"}
    """
    prompt = f"""
    You are an assistant that converts natural language into structured calendar actions.
    Input: "{message}"
    Output format: JSON with keys:
    - action: create_event, list_events, small_talk
    - title (if event)
    - date (YYYY-MM-DD)
    - time (HH:MM 24hr)
    """

    response = client.responses.create(
        model="o3-mini",  # or gpt-4.1-mini
        input=prompt
    )

    return response.output_parsed if hasattr(response, "output_parsed") else response.output_text
