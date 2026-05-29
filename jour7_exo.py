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
        secondes = (temps-int(temps))*60
        print(f"Temps voiture {self.marque} {self.modele} : {int(temps)} minutes et {secondes:.2f} sec.")
        self.temps += temps
        self.tour +=1

circuit = Circuit(10, 20)
voiture_1 = Voiture(80, 130, "Truc", "Mini")
voiture_2 = Voiture(70, 140, "Brol", "VW")
voiture_3 = Voiture(75, 135, "Machin", "Honda")
voiture_4 = Voiture(85, 125, "Plop", "Toyoto")
voiture_5 = Voiture(90, 115, "Clac", "Vrouvroum")

les_voitures = [voiture_1, voiture_2, voiture_3, voiture_4, voiture_5]

for i in range(circuit.tour):
    print(f"Tour: {i+1}")
    for v in les_voitures:
        v.roule_un_tour(circuit)


meilleur_temps = 1000000
voiture_gagnante = []
for v in les_voitures:
    if v.temps < meilleur_temps:
        meilleur_temps = v.temps
        voiture_gagnante = [v.marque, v.modele]

print(f"la voiture {voiture_gagnante[0]} {voiture_gagnante[1]} gagne la course avec un temps de {meilleur_temps:.2f} minutes")