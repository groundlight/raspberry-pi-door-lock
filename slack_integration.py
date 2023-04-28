import requests
import os
from logic import OPEN_TIME, CLOSE_TIME, TIMEZONE

def check_slack() -> bool:
    '''
    checks if slack integration is configured. Returns True and prints a helpful message about reporting times if it is configured. Otherwise it returns False and prints a helpful message about configuring slack
    '''

    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    if webhook_url:
        print(
            f"Slack integration is configured. You will receive slack messages about the door being unlocked outside of business hours {OPEN_TIME} to {CLOSE_TIME} in the {TIMEZONE} timezone. If you would like to change these times, edit the OPEN_TIME, CLOSE_TIME, and TIMEZONE variables in logic.py" 
        )
        return True
    else:
        print(
            "Slack integration is not configured. If you would like to receive slack messages about the door being unlocked outside of business hours, set the SLACK_WEBHOOK_URL environment variable by running `export SLACK_WEBHOOK_URL=your_webhook_url` before using this. You can learn about setting up a slack webhook at https://api.slack.com/messaging/webhooks"
        )
        return False


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
