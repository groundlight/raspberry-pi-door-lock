from photo import take_photo
from logic import is_door_locked, is_business_hours
import time
from picamera import PiCamera
import os
from slack_integration import send_slack_message

# get the API token from the environment and raise an error if it's not set
# api_token = "abc"  # os.environ.get("GROUNDLIGHT_API_TOKEN")

# if not api_token:
#     raise EnvironmentError(
#         "No API token found. Set the API_TOKEN environment variable by running `export api_token=your_token_value`  before running this script."
#     )


camera = PiCamera()
while True:
    image = take_photo(camera)
    is_locked = is_door_locked(image=image)

    if is_locked is None:
        print("Couldn't determine if the door is locked")

    elif is_locked is not None:
        if is_locked and is_business_hours():
            print(
                "The door is locked and it's business hours, someone should unlock it"
            )

        elif not is_locked and not is_business_hours():
            message = "The door is unlocked and it's not business hours, someone should lock it"
            print(message)

            # send the message to slack as we shouldn't leave the door unlocked after hours if the webhook url is set
            if os.environ.get("SLACK_WEBHOOK_URL"):
                send_slack_message(message=message)

        else:
            print("Everything is fine!")

    # sleep for 5 minutes before checking again
    time.sleep(5 * 60)
