from random import random


class SomeModel:
    def predict(self, message: str) -> float:
        if message == "something cool":
            return 100
        return random()
