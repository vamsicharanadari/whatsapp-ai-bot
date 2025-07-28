from fastapi import FastAPI, Request
import requests
from ai_handler import parse_user_message
from calendar_handler import create_event
from config import WHATSAPP_TOKEN, PHONE_NUMBER_ID, VERIFY_TOKEN

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# Helper: Send WhatsApp message
def send_message(to, message):
    url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
    headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}", "Content-Type": "application/json"}
    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }
    requests.post(url, headers=headers, json=data)


# 1. Verification (GET)
@app.get("/webhook")
async def verify(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return int(challenge)
    return {"status": "verification failed"}


# 2. Message Handler (POST)
@app.post("/webhook")
async def webhook(request: Request):
    body = await request.json()
    print("Incoming message:", body)

    # Extract user message
    try:
        message = body["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
        from_number = body["entry"][0]["changes"][0]["value"]["messages"][0]["from"]

        # Example reply
        send_message(from_number, f"You said: {message}")
    except Exception as e:
        print("No message content:", e)

    return {"status": "received"}
