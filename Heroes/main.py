from Entity.De import De
from Entity.Dragonnet import Dragonnet 
from Entity.Hero import Hero
from Entity.Humain import Humain
from Entity.Loup import Loup
from Entity.Monstre import Monstre
from Entity.Nain import Nain
from Entity.Orque import Orque
from Entity.Personnage import Personnage
from Entity.Zone import Zone
from random import randint

# from Entity import De --->  avec le __init__.py

zone = Zone()

mon_hero = Humain()

monstres = []
for i in range(10):
    rand = randint(0, 2)
    if rand == 0:
        monstre = Loup()
    elif rand == 1:
        monstre = Orque()
    else:
        monstre = Dragonnet()
    monstres.append(monstre)

zone.positionner_monstres(monstres)
zone.positionner_hero(mon_hero)
# print(zone.positions_monstres)

print("Le hero:", mon_hero)

while len(monstres) > 0 and mon_hero.pv > 0:
    # print(mon_hero.__class__.__name__, mon_hero, sep = ': ')
    # print(monstres[-1].__class__.__name__, monstres[-1], sep = ": " )
    # print(monstres)
    for i in zone.area:
        for j in i:
            print(j, sep='', end='')
        print(end='\n')

    direction = input('Quelle direction ? (h,b,d,g) ')
    mon_hero.move(direction, zone)

    ze_monstre = mon_hero.adistancedemonstre(zone)
    if ze_monstre:
        if monstre.__class__.__name__ == 'Loup':
            zone.area[ze_monstre.x][ze_monstre.y] = 'L'
        elif monstre.__class__.__name__ == 'Orque':
            zone.area[ze_monstre.x][ze_monstre.y] = 'O'
        if monstre.__class__.__name__ == 'Dragonnet':
            zone.area[ze_monstre.x][ze_monstre.y] = 'D'
        while ze_monstre.pv > 0 and mon_hero.pv > 0:
            mon_hero.frappe(ze_monstre)
            if ze_monstre.pv <= 0:
                print("monstre mort")
                mon_hero.repos()
                mon_hero.gold += ze_monstre.gold
                mon_hero.depecer(ze_monstre)
                monstres.pop()

                # zone.area[ze_monstre.x][ze_monstre.y] = '.'
                zone.positions_monstres.pop(ze_monstre.x, ze_monstre.y) 

            else:
                ze_monstre.frappe(mon_hero)
                if mon_hero.pv <= 0:
                    zone.area[mon_hero.x][mon_hero.y] = '\u271D'
                    print("hero mort")
    
if mon_hero.pv > 0:
    print('Victoire')
else:
<<<<<<< HEAD
=======
    zone.area[mon_hero.x][mon_hero.y] = "\u271d"
>>>>>>> 446c3ca8dacd5766cb84a512a2a63b5f33a1950b
    for i in zone.area:
        for j in i:
            print(j, sep='', end='')
        print(end='\n')
    print('Défaite')
print(mon_hero)
