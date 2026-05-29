from random import randint

class Personnage:
    def __init__(self, x=0, y=0):
        force = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
        force.remove(min(force))
        endurance = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
        endurance.remove(min(endurance))

        self._endurance = sum(endurance)
        self._force = sum(force)
    
        self.bonus_force = 0
        if self._force < 5:
            self.bonus_force = -1
        elif self._force >= 10 and self._force < 15:
            self.bonus_force = 1
        elif self._force >= 15:
            self.bonus_force = 2

        self.bonus_endurance = 0
        if self._endurance < 5:
            self.bonus_endurance = -1
        elif self._endurance >= 10 and self._endurance < 15:
            self.bonus_endurance = 1
        elif self._endurance >= 15:
            self.bonus_endurance = 2

        self.__pv = self._endurance + self.bonus_endurance
        self.gold = 0
        self.cuir = 0

        self.x = x
        self.y = y


    @property
    def pv(self):
        return self.__pv
    
    @pv.setter
    def pv(self, value):
        self.pv = value

    @property
    def endurance(self):
        return self._endurance
    
    @property
    def force(self):
        return self._force

    def frappe(self, autre):
        degats = randint(1, 4) + self.bonus_force
        autre.pv -= degats 

    def __str__(self):
        return f"Endurance= {self._endurance}, Force= {self._force}, Pv= {self.__pv}, gold= {self.gold}, cuir= {self.cuir}, position=({self.x, self.y}) "
