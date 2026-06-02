from random import randint
from Entity.De import De

class Personnage:
    def __init__(self, x=0, y=0):
        force = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
        force.remove(min(force))
        endurance = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
        endurance.remove(min(endurance))
        
        self._endurance = sum(endurance)
        self._force = sum(force)

        # self.__stamina = self.generate_stats() -->best pratctice
        # self.__strength = self.generate_stats()
        # self.__max_hp = self.stamina + self.modifier(self.stamina)
        # self.__hp = self.__max_hp
    
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

    def generate_stats(self):
        dice = De()
        return dice.roll_best_3_of_x(4)
    
    def modifier(self, base):
        modif = 0
        if base < 5:
            modif = -1
        elif base >= 10 and base < 15:
            modif = 1
        elif base >= 15:
            modif = 2

        return modif

    @property
    def pv(self):
        return self.__pv
    
    @pv.setter
    def pv(self, value):
        self.__pv = value  # max(0, min(value, self.max_hp))

    @property
    def endurance(self):
        return self._endurance
    
    @property
    def force(self):
        return self._force
    
    @property
    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp -= damage 

    def attack(self, target: "Personnage"):
        dice = De(4)
        damage = dice.roll() + self.modifier(self.strength)

        if damage < 0:
            damage = 0

        target.take_damage(damage)

    def frappe(self, autre):
        degats = randint(1, 4) + self.bonus_force
        autre.pv -= degats 
        print(f"{self.__class__.__name__} frappe de {degats} dégats sur {autre.__class__.__name__}")

    def __str__(self):
        return f"Endurance= {self._endurance}, Force= {self._force}, Pv= {self.__pv}, gold= {self.gold}, cuir= {self.cuir}, position=({self.x, self.y}) "

    def __repr__(self):
        return f'ENTITY name  stamina = {self._endurance}'
    