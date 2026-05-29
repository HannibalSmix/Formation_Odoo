from random import randint
from Entity.Monstre import Monstre

class Dragonnet(Monstre):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self._endurance += 1
        self.gold = randint(1, 6)
        self.cuir = randint(1, 4)

    def depecer(self):
        return self.cuir