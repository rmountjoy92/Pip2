from .procedural_face import ProceduralFace
from src.enums import ExpressionTypes


def get(name):
    """Returns an instance of a face expression.

    for example: expression = get("Happy")
    """
    import sys

    current_module = sys.modules[__name__]
    return getattr(current_module, name)()


class Base(ProceduralFace):
    pass


class Neutral(ProceduralFace):
    name = ExpressionTypes.NEUTRAL

    def __init__(self):
        super().__init__()
        self.eyes[0].scale_x = 0.8
        self.eyes[0].scale_y = 0.8
        self.eyes[1].scale_x = 0.8
        self.eyes[1].scale_y = 0.8


class Anger(ProceduralFace):
    name = ExpressionTypes.ANGER

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].y = 0.6
        self.eyes[0].lids[0].angle = -30.0
        self.eyes[1].lids[0].y = 0.6
        self.eyes[1].lids[0].angle = 30.0


class Sadness(ProceduralFace):
    name = ExpressionTypes.SADNESS

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].y = 0.6
        self.eyes[0].lids[0].angle = 20.0
        self.eyes[1].lids[0].y = 0.6
        self.eyes[1].lids[0].angle = -20.0


class Happy(ProceduralFace):
    name = ExpressionTypes.HAPPY

    def __init__(self):
        super().__init__()
        self.eyes[0].upper_outer_radius_x = 1.0
        self.eyes[0].upper_inner_radius_x = 1.0
        self.eyes[0].lids[1].y = 0.4
        self.eyes[0].lids[1].bend = 0.4
        self.eyes[1].upper_outer_radius_x = 1.0
        self.eyes[1].upper_inner_radius_x = 1.0
        self.eyes[1].lids[1].y = 0.4
        self.eyes[1].lids[1].bend = 0.4


class Surprise(ProceduralFace):
    name = ExpressionTypes.SURPRISE

    def __init__(self):
        super().__init__()
        self.eyes[0].scale_x = 1.25
        self.eyes[0].scale_y = 1.25
        self.eyes[1].scale_x = 1.25
        self.eyes[1].scale_y = 1.25


class Disgust(ProceduralFace):
    name = ExpressionTypes.DISGUST

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].y = 0.3
        self.eyes[0].lids[0].angle = 10.0
        self.eyes[0].lids[1].y = 0.3
        self.eyes[1].lids[0].y = 0.2
        self.eyes[1].lids[0].angle = 20.0
        self.eyes[1].lids[1].y = 0.2
        self.eyes[1].lids[1].angle = 10.0


class Fear(ProceduralFace):
    name = ExpressionTypes.FEAR

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].angle = 30.0
        self.eyes[0].lids[0].bend = 0.1
        self.eyes[0].lids[1].y = 0.4
        self.eyes[0].lids[1].angle = 10.0
        self.eyes[1].lids[0].angle = -30.0
        self.eyes[1].lids[0].bend = 0.1
        self.eyes[1].lids[1].y = 0.4
        self.eyes[1].lids[1].angle = -10.0


class Pleading(ProceduralFace):
    name = ExpressionTypes.PLEADING

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].angle = 30.0
        self.eyes[0].lids[1].y = 0.5
        self.eyes[1].lids[0].angle = -30.0
        self.eyes[1].lids[1].y = 0.5


class Vulnerability(ProceduralFace):
    name = ExpressionTypes.VULNERABILITY

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].angle = 20.0
        self.eyes[0].lids[0].y = 0.3
        self.eyes[0].lids[1].angle = 10.0
        self.eyes[0].lids[1].y = 0.5
        self.eyes[1].lids[0].angle = -20.0
        self.eyes[1].lids[0].y = 0.3
        self.eyes[1].lids[1].angle = -10.0
        self.eyes[1].lids[1].y = 0.5


class Despair(ProceduralFace):
    name = ExpressionTypes.DESPAIR

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].angle = 30.0
        self.eyes[0].lids[0].y = 0.6
        self.eyes[1].lids[0].angle = -30.0
        self.eyes[1].lids[0].y = 0.6


class Guilt(ProceduralFace):
    name = ExpressionTypes.GUILT

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].angle = 10.0
        self.eyes[0].lids[0].y = 0.6
        self.eyes[0].lids[0].bend = 0.3
        self.eyes[1].lids[0].angle = -10.0
        self.eyes[1].lids[0].y = 0.6
        self.eyes[1].lids[0].bend = 0.3


class Disappointment(ProceduralFace):
    name = ExpressionTypes.DISAPPOINTMENT

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].angle = -10.0
        self.eyes[0].lids[0].y = 0.3
        self.eyes[0].lids[1].y = 0.4
        self.eyes[1].lids[0].angle = 10.0
        self.eyes[1].lids[0].y = 0.3
        self.eyes[1].lids[1].y = 0.4


class Embarrassment(ProceduralFace):
    name = ExpressionTypes.EMBARRASSMENT

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].angle = 10.0
        self.eyes[0].lids[0].y = 0.5
        self.eyes[0].lids[0].bend = 0.1
        self.eyes[0].lids[1].y = 0.1
        self.eyes[1].lids[0].angle = -10.0
        self.eyes[1].lids[0].y = 0.5
        self.eyes[1].lids[0].bend = 0.1
        self.eyes[1].lids[1].y = 0.1


class Horror(ProceduralFace):
    name = ExpressionTypes.HORROR

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].angle = 20.0
        self.eyes[1].lids[0].angle = -20.0


class Skepticism(ProceduralFace):
    name = ExpressionTypes.SKEPTICISM

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].angle = -10.0
        self.eyes[0].lids[0].y = 0.4
        self.eyes[1].lids[0].angle = 25.0
        self.eyes[1].lids[0].y = 0.15


class Annoyance(ProceduralFace):
    name = ExpressionTypes.ANNOYANCE

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].angle = -30.0
        self.eyes[0].lids[1].angle = -10.0
        self.eyes[0].lids[1].y = 0.3
        self.eyes[1].lids[0].angle = 30.0
        self.eyes[1].lids[0].y = 0.2
        self.eyes[1].lids[1].angle = 5.0
        self.eyes[1].lids[1].y = 0.4
        self.eyes[1].upper_inner_radius_x = 1.0
        self.eyes[1].upper_outer_radius_x = 1.0


class Fury(ProceduralFace):
    name = ExpressionTypes.FURY

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].angle = -30.0
        self.eyes[0].lids[0].y = 0.3
        self.eyes[0].lids[1].y = 0.4
        self.eyes[1].lids[0].angle = 30.0
        self.eyes[1].lids[0].y = 0.3
        self.eyes[1].lids[1].y = 0.4


class Suspicion(ProceduralFace):
    name = ExpressionTypes.SUSPICION

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].angle = -10.0
        self.eyes[0].lids[0].y = 0.4
        self.eyes[0].lids[1].y = 0.5
        self.eyes[1].lids[0].angle = 10.0
        self.eyes[1].lids[0].y = 0.4
        self.eyes[1].lids[1].y = 0.5


class Rejection(ProceduralFace):
    name = ExpressionTypes.REJECTION

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].angle = 25.0
        self.eyes[0].lids[0].y = 0.8
        self.eyes[1].lids[0].angle = 25.0
        self.eyes[1].lids[0].y = 0.8


class Boredom(ProceduralFace):
    name = ExpressionTypes.BOREDOM

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].y = 0.4
        self.eyes[1].lids[0].y = 0.4


class Tired(ProceduralFace):
    name = ExpressionTypes.TIRED

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[0].angle = 5.0
        self.eyes[0].lids[0].y = 0.4
        self.eyes[0].lids[1].y = 0.5
        self.eyes[1].lids[0].angle = -5.0
        self.eyes[1].lids[0].y = 0.4
        self.eyes[1].lids[1].y = 0.5


class Asleep(ProceduralFace):
    name = ExpressionTypes.ASLEEP

    def __init__(self):
        super().__init__()
        self.eyes[0].center_y = 50.0
        self.eyes[0].lids[0].y = 0.45
        self.eyes[0].lids[1].y = 0.5
        self.eyes[1].center_y = 50.0
        self.eyes[1].lids[0].y = 0.45
        self.eyes[1].lids[1].y = 0.5


class Confused(ProceduralFace):
    name = ExpressionTypes.CONFUSED

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[1].y = 0.2
        self.eyes[0].lids[1].bend = 0.2
        self.eyes[1].lids[0].angle = -10.0
        self.eyes[1].lids[0].y = 0.3
        self.eyes[1].lids[1].angle = 5.0
        self.eyes[1].lids[1].y = 0.2
        self.eyes[1].lids[1].bend = 0.2


class Amazed(ProceduralFace):
    name = ExpressionTypes.AMAZED

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[1].y = 0.2
        self.eyes[1].lids[1].y = 0.2


class Excited(ProceduralFace):
    name = ExpressionTypes.EXCITED

    def __init__(self):
        super().__init__()
        self.eyes[0].lids[1].y = 0.3
        self.eyes[0].lids[1].bend = 0.2
        self.eyes[1].lids[1].y = 0.3
        self.eyes[1].lids[1].bend = 0.2
