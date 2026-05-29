from random import randint

class De:
    def __init__(self, max):
        self.minimum = 1
        self.maximum = max

    def lancer(self):
        return randint(self.minimum, self.maximum)