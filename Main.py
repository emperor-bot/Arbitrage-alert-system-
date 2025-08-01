import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_IDS = os.getenv("CHAT_IDS").split(",")

def send_alert(message):
    for chat_id in CHAT_IDS:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {"chat_id": chat_id, "text": message}
        requests.post(url, data=data)

if __name__ == "__main__":
    send_alert("✅ Test alert: Bot is running and ready!")
