import sys
import asyncio
import random

from .procedural_face import ProceduralFace
from . import expressions
from src.enums import ExpressionTypes, AnimationTypes


class BaseAnimation:
    name = AnimationTypes.BASE
    eye_manager = None
    max_x_offset = 200
    max_y_offset = 300

    def __init__(self, eye_manager):
        self.eye_manager = eye_manager

    async def play(self):
        self.eye_manager.set_next_expression(ExpressionTypes.NEUTRAL)


def get_animation(animation_name: str):
    current_module = sys.modules[__name__]
    return getattr(current_module, animation_name)


class LookRight(BaseAnimation):
    name = AnimationTypes.LOOK_RIGHT

    async def play(
        self,
        distance: int = 190,
        duration: float = 0.25,
        pause_duration: float = 2.0,
        return_duration: float = 0.25,
    ):
        current_face = expressions.get(self.eye_manager.current_face.name)
        next_face = ProceduralFace(list(self.eye_manager.current_face.params))

        next_face.eyes[0].center_x += distance + 30
        next_face.eyes[1].center_x += distance

        next_face.eyes[0].scale_x = min(
            current_face.eyes[0].scale_x,
            current_face.eyes[0].scale_x - (distance / 190) * 0.3,
        )
        next_face.eyes[1].scale_x = min(
            current_face.eyes[1].scale_x,
            current_face.eyes[1].scale_x - (distance / 190) * 0.5,
        )

        self.eye_manager.set_next_expression(
            expression_class=next_face, duration=duration
        )
        await asyncio.sleep(pause_duration)
        self.eye_manager.set_next_expression(
            expression_class=current_face, duration=return_duration
        )


class LookLeft(BaseAnimation):
    name = AnimationTypes.LOOK_LEFT

    async def play(
        self,
        distance: int = 190,
        duration: float = 0.25,
        pause_duration: float = 2.0,
        return_duration: float = 0.25,
    ):
        current_face = expressions.get(self.eye_manager.current_face.name)
        next_face = ProceduralFace(list(self.eye_manager.current_face.params))

        next_face.eyes[1].center_x -= distance + 30
        next_face.eyes[0].center_x -= distance

        next_face.eyes[1].scale_x = min(
            current_face.eyes[1].scale_x,
            current_face.eyes[1].scale_x - (distance / 190) * 0.3,
        )
        next_face.eyes[0].scale_x = min(
            current_face.eyes[0].scale_x,
            current_face.eyes[0].scale_x - (distance / 190) * 0.5,
        )

        self.eye_manager.set_next_expression(
            expression_class=next_face, duration=duration
        )
        await asyncio.sleep(pause_duration)
        self.eye_manager.set_next_expression(
            expression_class=current_face, duration=return_duration
        )


class LookDown(BaseAnimation):
    name = AnimationTypes.LOOK_DOWN

    async def play(
        self,
        distance: int = 190,
        duration: float = 0.25,
        pause_duration: float = 2.0,
        return_duration: float = 0.25,
    ):
        current_face = expressions.get(self.eye_manager.current_face.name)
        next_face = ProceduralFace(list(self.eye_manager.current_face.params))

        next_face.eyes[0].center_x += 20
        next_face.eyes[1].center_x -= 20

        next_face.eyes[1].center_y += distance
        next_face.eyes[0].center_y += distance

        self.eye_manager.set_next_expression(
            expression_class=next_face, duration=duration
        )
        await asyncio.sleep(pause_duration)
        self.eye_manager.set_next_expression(
            expression_class=current_face, duration=return_duration
        )


class LookUp(BaseAnimation):
    name = AnimationTypes.LOOK_UP

    async def play(
        self,
        distance: int = 190,
        duration: float = 0.25,
        pause_duration: float = 2.0,
        return_duration: float = 0.25,
    ):
        current_face = expressions.get(self.eye_manager.current_face.name)
        next_face = ProceduralFace(list(self.eye_manager.current_face.params))

        next_face.eyes[1].center_y -= distance
        next_face.eyes[0].center_y -= distance

        next_face.eyes[0].center_x += 30
        next_face.eyes[1].center_x -= 30

        self.eye_manager.set_next_expression(
            expression_class=next_face, duration=duration
        )
        await asyncio.sleep(pause_duration)
        self.eye_manager.set_next_expression(
            expression_class=current_face, duration=return_duration
        )


class Blink(BaseAnimation):
    name = AnimationTypes.BLINK

    async def play(self):
        current_face = expressions.get(self.eye_manager.current_face.name)
        next_face = ProceduralFace(list(self.eye_manager.current_face.params))

        next_face.scale_y = 0
        next_face.eyes[0].scale_x = 1
        next_face.eyes[1].scale_x = 1
        next_face.eyes[0].scale_y = 0
        next_face.eyes[1].scale_y = 0

        self.eye_manager.set_next_expression(expression_class=next_face, duration=0.15)
        await asyncio.sleep(0.15)
        self.eye_manager.set_next_expression(
            expression_class=current_face, duration=0.1
        )


class Saccade(BaseAnimation):
    name = AnimationTypes.SACCADE

    async def play(self):
        choices = [LookLeft, LookRight, LookDown, LookUp]
        choice = random.choice(choices)(self.eye_manager)
        if choice.name in [AnimationTypes.LOOK_LEFT, AnimationTypes.LOOK_RIGHT]:
            await choice.play(
                distance=random.uniform(0, self.max_x_offset),
                duration=random.uniform(0.25, 0.5),
                pause_duration=random.uniform(1, 2),
                return_duration=random.uniform(0.25, 0.5),
            )
        if choice.name in [AnimationTypes.LOOK_DOWN, AnimationTypes.LOOK_UP]:
            await choice.play(
                distance=random.uniform(0, self.max_y_offset),
                duration=random.uniform(0.25, 0.5),
                pause_duration=random.uniform(0.25, 4),
                return_duration=random.uniform(0.25, 0.5),
            )
