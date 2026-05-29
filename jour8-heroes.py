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

class Hero(Personnage):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.pvmax = self.pv
        
    def frappe(self, autre):
        super().frappe(autre)
        if autre.pv <= 0:
            self.gold += autre.gold
            self.cuir += autre.cuir

    def repos(self):
        self.pv = self.pvmax

class Humains(Hero):
    def __init__(self, x=0, y=0):
        super().__init__(x, y) 
        self._endurance += 1
        self._force += 1     

class Nain(Hero):
    def __init__(self, x=0, y=0):
        super().__init__(x, y) 
        self._endurance += 2   

class Monstre(Personnage):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

class Loup(Monstre):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.cuir = randint(1, 4)

    def depecer(self):
        return self.cuir
    
class Orque(Monstre):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self._force += 1
        self.gold = randint(1, 6)

class Dragonnet(Monstre):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self._endurance += 1
        self.gold = randint(1, 6)
        self.cuir = randint(1, 4)

    def depecer(self):
        return self.cuir

class de:
    def __init__(self, max):
        self.minimum = 1
        self.maximum = max

    def lancer(self):
        return randint(self.minimum, self.maximum)
    

