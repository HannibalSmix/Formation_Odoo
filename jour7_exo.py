import random

class Course():
    pass

class Circuit():
    def __init__(self, distance, tour):
        self.distance = distance
        self.tour = tour

class Voiture():
    def __init__(self, vitesse_min, vitesse_max, modele, marque):
        self.vitesse_min = vitesse_min
        self.vitesse_max = vitesse_max
        self.modele = modele
        self.marque = marque
        self.tour = 0
        self.temps = 0

    def roule_un_tour(self, circuit):
        vitesse_rand = random.randint(self.vitesse_min, self.vitesse_max)
        temps = 60 * circuit.distance / vitesse_rand 
        print(f"Temps voiture {self.marque} {self.modele} : {temps}")
        self.temps += temps
        self.tour +=1



circuit = Circuit(10, 20)
Voiture_1 = Voiture(80, 120, "Truc", "Mini")
Voiture_2 = Voiture(70, 140, "Brol", "VW")
Voiture_3 = Voiture(75, 135, "Machin", "Honda")
Voiture_4 = Voiture(90, 160, "Plop", "Toyoto")
Voiture_5 = Voiture(100, 145, "Clac", "Vrouvroum")

les_voitures = [Voiture_1,Voiture_1,Voiture_1,Voiture_1,Voiture_5]

for i in range(circuit.tour):
    Voiture_1.roule_un_tour(circuit)
    Voiture_2.roule_un_tour(circuit)
    Voiture_3.roule_un_tour(circuit)
    Voiture_4.roule_un_tour(circuit)
    Voiture_5.roule_un_tour(circuit)

