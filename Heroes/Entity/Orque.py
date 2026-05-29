from random import randint
from Entity.Monstre import Monstre

class Orque(Monstre):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self._force += 1
        self.gold = randint(1, 6)