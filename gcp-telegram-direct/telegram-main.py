import base64
import json
import requests
import functions_framework

# Telegram details
TELEGRAM_BOT_TOKEN = "123456789:AAH...xyz"  # Apna token daal do
TELEGRAM_CHAT_ID = "-987654321"              # Apna chat ID daal do

@functions_framework.cloud_event
def telegram_alert(cloud_event):
    pubsub_message = base64.b64decode(cloud_event.data["message"]["data"]).decode('utf-8')
    pubsub_data = json.loads(pubsub_message)
    
    status = pubsub_data.get("status", "Unknown")
    trigger_name = pubsub_data.get("substitutions", {}).get("TRIGGER_NAME", "Unknown Trigger")
    repo_name = pubsub_data.get("substitutions", {}).get("REPO_NAME", "Unknown Repo")
    
    message = f"{repo_name} ka trigger '{trigger_name}' hua hai\nAur {status.lower()} hua hai"
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Error: {response.status_code} {response.text}")
