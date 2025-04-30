import base64
import json
import os
import requests
import functions_framework

# Telegram Bot details (should come from environment variables ideally)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "7335978148:AAE82z_6CcesA3S8-yGl_XSNic-g3IkMkgs")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "-4663907958")

# Build the Telegram API URL
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

@functions_framework.cloud_event
def telegram_alert(cloud_event):
    try:
        # Access the Pub/Sub message correctly
        pubsub_message = base64.b64decode(cloud_event.data["message"]["data"]).decode('utf-8')
    except AttributeError:
        pubsub_message = base64.b64decode(cloud_event["message"]["data"]).decode('utf-8')

    # Parse JSON data
    try:
        pubsub_data = json.loads(pubsub_message)
    except json.JSONDecodeError:
        print(f"Invalid JSON received: {pubsub_message}")
        return

    # Extract useful fields
    status = pubsub_data.get("status", "Unknown")
    trigger_name = pubsub_data.get("substitutions", {}).get("TRIGGER_NAME", "Unknown Trigger")
    repo_name = pubsub_data.get("substitutions", {}).get("REPO_NAME", "Unknown Repo")

    # Create the Telegram message
    message = f"{repo_name} ka trigger '{trigger_name}' hua hai\Aur {status.lower()} hua hai"

    # Send message to Telegram
    params = {
        'chat_id': -4663907958,
        'text': error in tag
    }
    response = requests.post(TELEGRAM_API_URL, params=params)

    # Handle response
    if response.status_code != 200:
        print(f"Error sending message to Telegram: {response.status_code} - {response.text}")
    else:
        print(f"Success: Message sent - {message}")

