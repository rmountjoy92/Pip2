import asyncio
import random
import time
from io import BytesIO

from src.enums import AnimationTypes
from src.enums import ExpressionTypes
from . import expressions as exp
from . import procedural_face as pf
from .animations import get_animation
from ..base_service import PipService


class EyeManager(PipService):
    def __init__(self, pip):
        super().__init__(pip)
        self.ideal_FPS = 60

        self.current_face = exp.Neutral()
        self.next_expression = None

        self.time_since_last_blink = 0
        self.time_since_last_saccade = 0
        self.is_interpolating = False
        self.face_generator = None
        self.animation_event = asyncio.Event()

    async def generate_eye_steam(self):
        elapsed_time = 0
        while True:
            begin_time = time.time()
            face = self.step(elapsed_time * 1000)

            # Render the face to an PIL image
            pil_image = face.render()

            # Convert PIL image to bytes
            image_bytes = BytesIO()
            pil_image.save(image_bytes, format="JPEG")
            image_bytes = image_bytes.getvalue()

            # Yield the frame in the required format
            yield b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + image_bytes + b"\r\n"

            await asyncio.sleep(0.016)

            elapsed_time = time.time() - begin_time

    def set_next_expression(
        self,
        expression_name: str = None,
        expression_class: pf.ProceduralFace = None,
        duration: int = 1,
    ):
        """Create a face_list array (the number of frames is calculated
        according to the duration time)

        This function takes two variables: expression and duration time. While
        the expression is a procedural face object, duration needs to be given
        as seconds.
        """

        number_of_frames = int(duration * self.ideal_FPS)
        self.next_expression = (
            expression_class if expression_class else exp.get(expression_name)
        )
        self.face_generator = pf.interpolate(
            self.current_face, self.next_expression, number_of_frames
        )
        self.is_interpolating = True

    # Idle State
    def step(self, elapsed_time):
        """:param elapsed_time: elapsed time since last call to step, in milliseconds."""

        nb_frames_to_skip = int(elapsed_time * self.ideal_FPS / 1000.0)

        idx = 0

        for face in self.face_generator:
            if idx == nb_frames_to_skip:
                self.current_face = face
                break
            idx += 1

        if (
            self.is_interpolating and idx < nb_frames_to_skip
        ):  # we are at the end of the interpolation
            self.current_face = self.next_expression
            self.is_interpolating = False

        return self.current_face

    async def process_idle(self):
        while True:
            self.time_since_last_saccade += 1
            self.time_since_last_blink += 1
            # Blinking
            no_blink = [ExpressionTypes.ANGER, ExpressionTypes.ASLEEP]
            if (
                self.current_face.name not in no_blink
                and self.time_since_last_blink > random.randint(6, 14)
            ):
                await self.animate(AnimationTypes.BLINK)
                self.time_since_last_blink = 0

            # Saccades
            no_saccade = [ExpressionTypes.ASLEEP]
            if (
                self.current_face.name not in no_saccade
                and self.time_since_last_saccade > random.randint(6, 14)
            ):
                await self.animate(AnimationTypes.SACCADE)
                self.time_since_last_saccade = 0
            await asyncio.sleep(1)

    async def animate(self, animation_name: AnimationTypes):
        if not self.animation_event.is_set() and not self.is_interpolating:
            self.animation_event.set()
            try:
                animation_class = get_animation(animation_name)
                await animation_class(self).play()
            except Exception as e:
                print(f"Error during animation: {e}")
            finally:
                self.animation_event.clear()
