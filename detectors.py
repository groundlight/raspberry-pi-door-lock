from pydantic import BaseModel


class GroundlightDetector(BaseModel):
    name: str
    query: str
    confidence: float


door_locked_detector = GroundlightDetector(
    name="door_locked_detector",
    query="Is the door locked?",
    confidence=0.9,
)
