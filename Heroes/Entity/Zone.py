from random import randint

class Zone:
    def __init__(self):
        self.width = 15
        self.height = 15
        self.area = [['.' for _ in range(15)] for _ in range(15)]
        self.positions_monstres = {}
        self.positions_heros = []

    def positionner_monstres(self, monstres):
        for monstre in monstres:
            position_trouvee = True
            while position_trouvee:
                x = randint(0, 14)
                y = randint(0, 14)
                if (x, y) not in self.positions_monstres:
                    enough_space = True
                    for x1, y1 in self.positions_monstres:
                        if abs(x-x1) + abs(y-y1) <= 2:
                            enough_space = False
                            break
                    if enough_space:
                        position_trouvee = False
                        self.positions_monstres[(x, y)] = monstre
                        monstre.x = x
                        monstre.y = y
                        if monstre.__class__.__name__ == 'Loup':
                            self.area[x][y] = '.'
                        elif monstre.__class__.__name__ == 'Orque':
                            self.area[x][y] = '.'
                        if monstre.__class__.__name__ == 'Dragonnet':
                            self.area[x][y] = '.'

    def positionner_hero(self, hero):
        position_trouvee = True
        while position_trouvee:
            x = randint(0, 14)
            y = randint(0, 14)
            if (x, y) not in self.positions_monstres:
                enough_space = True
                for x1, y1 in self.positions_monstres:
                    if abs(x-x1) + abs(y-y1) <= 2:
                        enough_space = False
                        break
                if enough_space:
                    if (x, y) not in self.positions_monstres and (x, y) not in self.positions_heros:
                        position_trouvee = False
                        self.positions_heros.append((x, y))
                        hero.x = x
                        hero.y = y
                        if hero.__class__.__name__ == 'Nain':
                            self.area[x][y] = 'N'
                        elif hero.__class__.__name__ == 'Humain':
                            self.area[x][y] = 'H'

    def monstreatposition(self, x, y):
        monstre = self.positions_monstres[(x, y)]
        if monstre:
            if monstre.__class__.__name__ == 'Loup':
                self.area[x][y] = 'L'
            elif monstre.__class__.__name__ == 'Orque':
                self.area[x][y] = 'O'
            if monstre.__class__.__name__ == 'Dragonnet':
                self.area[x][y] = 'D'

        return self.positions_monstres[(x, y)]

