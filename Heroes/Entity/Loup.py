
from random import randint
from Entity.Monstre import Monstre

class Loup(Monstre):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.cuir = randint(1, 4)

    def depecer(self):
        return self.cuir