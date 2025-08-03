from venv import logger

from src.core.pip.base_service import PipService
from src.enums import ExpressionTypes, EmotionTypes


class EmotionsManager(PipService):
    current_emotion: str = EmotionTypes.NEUTRAL
    emotion_level: int = 0

    def __init__(self, pip):
        super().__init__(pip)
        self.pip.eye_manager.set_next_expression(ExpressionTypes.NEUTRAL)

    emotions: dict = {
        EmotionTypes.NEUTRAL: {0: ExpressionTypes.NEUTRAL},
        EmotionTypes.HAPPY: {
            0: ExpressionTypes.AMAZED,
            1: ExpressionTypes.EXCITED,
            2: ExpressionTypes.HAPPY,
        },
        EmotionTypes.TIRED: {
            0: ExpressionTypes.BOREDOM,
            1: ExpressionTypes.TIRED,
            2: ExpressionTypes.ASLEEP,
        },
        EmotionTypes.ANGRY: {
            0: ExpressionTypes.SKEPTICISM,
            1: ExpressionTypes.ANNOYANCE,
            2: ExpressionTypes.ANGER,
            3: ExpressionTypes.FURY,
            4: ExpressionTypes.DISAPPOINTMENT,
        },
        EmotionTypes.SAD: {
            0: ExpressionTypes.GUILT,
            1: ExpressionTypes.VULNERABILITY,
            2: ExpressionTypes.FEAR,
            3: ExpressionTypes.SADNESS,
            4: ExpressionTypes.DESPAIR,
            5: ExpressionTypes.REJECTION,
        },
        EmotionTypes.CONFUSED: {
            0: ExpressionTypes.SURPRISE,
            1: ExpressionTypes.CONFUSED,
            2: ExpressionTypes.HORROR,
        },
    }

    def set_current_emotion(
        self,
        emotion: str = EmotionTypes.NEUTRAL,
        level: int = 0,
        max_level: bool = False,
    ):
        if max_level:
            emotion_levels = self.emotions.get(emotion)
            if not emotion_levels:
                raise Exception("Invalid emotion.")
            level = max(emotion_levels.keys())

        previous_expression = self.get_expression()
        self.current_emotion = emotion
        self.emotion_level = level
        new_expression = self.get_expression()
        if previous_expression != new_expression:
            logger.info(f"applying new expression: {new_expression}")
            self.pip.eye_manager.set_next_expression(new_expression)

    def get_current_emotion_for_thread(self):
        emotion_levels = self.emotions.get(self.current_emotion)
        if emotion_levels is None:
            return None
        max_level = max(emotion_levels.keys())
        return f"{self.current_emotion} Level: {self.emotion_level}/{max_level}"

    def get_expression(self):
        emotion_levels = self.emotions.get(self.current_emotion)
        if emotion_levels is None:
            return ExpressionTypes.NEUTRAL

        max_level = max(emotion_levels.keys())

        if self.emotion_level <= max_level:
            return emotion_levels[self.emotion_level]

        self.emotion_level = max_level
        return emotion_levels[max_level]

    def increase_emotion_level(self):
        emotion_levels = self.emotions.get(self.current_emotion)
        if emotion_levels is None:
            return

        max_level = max(emotion_levels.keys())

        if self.emotion_level < max_level:
            self.set_current_emotion(self.current_emotion, self.emotion_level + 1)

        return

    def decrease_emotion_level(self):
        emotion_levels = self.emotions.get(self.current_emotion)
        if emotion_levels is None:
            return

        if self.emotion_level > 0:
            self.set_current_emotion(self.current_emotion, self.emotion_level - 1)

        return

    def is_asleep(self):
        return self.current_emotion == EmotionTypes.TIRED and self.emotion_level == 2
