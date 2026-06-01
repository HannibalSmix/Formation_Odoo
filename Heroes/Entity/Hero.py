
from Entity.Personnage import Personnage

class Hero(Personnage):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.pvmax = self.pv
        
    def frappe(self, autre):
        super().frappe(autre)

    def repos(self):
        self.pv = self.pvmax

    def depecer(self, monstre):
        self.cuir += monstre.cuir

    def move(self, direction, zone):
        zone.area[self.x][self.y] = '.'
        match direction:
            case 'h':
                self.x -= 1
            case 'b':
                self.x += 1
            case 'g':
                self.y -= 1
            case 'd':
                self.y += 1

        zone.area[self.x][self.y] = 'H'

    def adistancedemonstre(self, zone):
        if (self.x+1, self.y) in zone.positions_monstres:
            return zone.monstreatposition(self.x+1, self.y)
        elif (self.x, self.y+1) in zone.positions_monstres:
            return zone.monstreatposition(self.x, self.y+1)
        elif (self.x, self.y-1) in zone.positions_monstres:
            return zone.monstreatposition(self.x, self.y-1)
        elif (self.x-1, self.y) in zone.positions_monstres:
            return zone.monstreatposition(self.x-1, self.y)
        else:
            return False

