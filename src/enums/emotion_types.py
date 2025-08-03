from enum import Enum


class EmotionTypes(str, Enum):
    NEUTRAL = "Neutral"
    HAPPY = "happy"
    TIRED = "tired"
    ANGRY = "angry"
    SAD = "sad"
    CONFUSED = "confused"
