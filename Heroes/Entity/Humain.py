
from Entity.Hero import Hero

class Humain(Hero):
    def __init__(self, x=0, y=0):
        super().__init__(x, y) 
        self._endurance += 1
        self._force += 1    

    def __str__(self):
        return super().__str__() 