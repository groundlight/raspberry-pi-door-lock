from photo import take_photo
from logic import is_door_locked, is_business_hours
import time
from picamera import PiCamera
import os
from slack_integration import send_slack_message, check_slack

# initialize the camera
camera = PiCamera()

# check if we should send slack messages
send_messages = check_slack()

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

            # send the message to slack as we shouldn't leave the door unlocked after hours
            if send_messages:
                send_slack_message(message=message)

        else:
            print("Everything is fine!")

    # sleep for 5 minutes before checking again
    time.sleep(5 * 60)
