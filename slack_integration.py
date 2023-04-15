import requests
import os


def send_slack_message(message: str):
    """
    Send a message to slack at the webhook url in the environment
    """
    data = {
        "text": message,
    }
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")

    if not webhook_url:
        raise EnvironmentError(
            "No webhook URL found. Set the SLACK_WEBHOOK_URL environment variable by running `export SLACK_WEBHOOK_URL=your_webhook_url`  before using this."
        )
    requests.post(webhook_url, json=data)
