from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image


def take_photo(camera) -> Image:
    """
    Take a photo with the camera and return a PIL image
    """

    # Create the in-memory stream
    stream = BytesIO()

    camera.capture(stream, format="jpeg")
    # "Rewind" the stream to the beginning so we can read its content
    stream.seek(0)
    image = Image.open(stream)

    # our camera is rotated 180 degrees, so we need to rotate the image
    image = image.rotate(180)
    return image
