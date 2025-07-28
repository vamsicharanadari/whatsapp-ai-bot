from dotenv import load_dotenv
import os

load_dotenv()  # loads variables from .env into environment

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
YOUR_OPENAI_API_KEY = os.getenv("YOUR_OPENAI_API_KEY")