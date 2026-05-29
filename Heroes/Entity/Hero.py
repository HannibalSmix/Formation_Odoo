
from Entity.Personnage import Personnage

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