class PipService:
    def __init__(self, pip):
        from src.core.pip import PipsBrain

        self.pip: PipsBrain = pip
