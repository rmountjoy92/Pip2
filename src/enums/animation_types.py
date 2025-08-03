from enum import Enum


class AnimationTypes(str, Enum):
    BASE = "BaseAnimation"
    LOOK_RIGHT = "LookRight"
    LOOK_LEFT = "LookLeft"
    LOOK_UP = "LookUp"
    LOOK_DOWN = "LookDown"
    BLINK = "Blink"
    SACCADE = "Saccade"
