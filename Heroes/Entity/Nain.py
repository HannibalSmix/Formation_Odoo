from Entity.Hero import Hero

class Nain(Hero):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self._endurance += 2