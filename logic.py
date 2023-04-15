from detectors import GroundlightDetector, door_locked_detector
from groundlight import Groundlight
from PIL import Image
from typing import Optional
import datetime
import pytz


def is_door_locked(image: Image) -> Optional[bool]:
    """
    Return True if the door is locked, False otherwise
    """
    detector_config: GroundlightDetector = door_locked_detector

    gl = Groundlight()

    # TODO be able to set confidence when creating the detector
    detector = gl.get_or_create_detector(
        name=detector_config.name, query=detector_config.query
    )

    try:
        image_query = gl.submit_image_query(image=image, detector=detector, wait=60)
    except Exception as e:
        print(f"Error submitting image query: {e}")
        return None

    result = image_query.result

    # if the confidence is too low, return None as we don't know the answer with enough confidence
    if result.confidence and result.confidence < detector_config.confidence:
        return None

    # otherwise, return if the door is locked
    return result.label == "PASS"


def is_business_hours() -> bool:
    """
    Return True if it's business hours, False otherwise
    """
    # groundlight office is in the US/Pacific timezone
    now = datetime.datetime.now(pytz.timezone("US/Pacific"))

    # it is business hours if it is between 9am and 5pm on a weekday
    if now.weekday() < 5 and 9 <= now.hour < 17:
        return True
    return False
