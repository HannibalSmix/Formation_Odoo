import random
import threading
import time


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
        print(f"Thread : {threading.current_thread().name}")
        print(f"Temps voiture {self.marque} {self.modele} : {int(temps)} minutes et {secondes:.2f} sec.")
        self.temps += temps
        self.tour +=1
        time.sleep(random.randint(1, 3))

    def roule(self, circuit):
        for i in range(circuit.tour):
            # print(f"Laps : {self.tour}, voiture : {self.marque} {self.modele} ")
            vitesse_rand = random.randint(self.vitesse_min, self.vitesse_max)
            temps = 60 * circuit.distance / vitesse_rand 
            secondes = (temps-int(temps))*60
            # print(f"Thread : {threading.current_thread().name}")
            print(f"Laps : {self.tour+1}, Temps voiture {self.marque} {self.modele} : {int(temps)} minutes et {secondes:.2f} sec.")
            self.temps += temps
            self.tour +=1
            time.sleep(temps)
            # time.sleep(random.randint(1, 3))


circuit = Circuit(1, 10)
voiture_1 = Voiture(80, 130, "Truc", "Mini")
voiture_2 = Voiture(70, 140, "Brol", "VW")
voiture_3 = Voiture(75, 135, "Machin", "Honda")
voiture_4 = Voiture(85, 125, "Plop", "Toyoto")
voiture_5 = Voiture(90, 115, "Clac", "Vrouvroum")
voiture_6 = Voiture(50, 90, "Carrémentnul", "Nunul")

les_voitures = [voiture_1, voiture_2, voiture_3, voiture_4, voiture_5, voiture_6]

threads = []
for voiture in les_voitures:
    t = threading.Thread(target=voiture.roule, args=(circuit,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

# t = threading.Thread(target=voiture_1.roule_un_tour, args=(circuit,))
# t2 = threading.Thread(target=voiture_2.roule_un_tour, args=(circuit,))
# t3 = threading.Thread(target=voiture_3.roule_un_tour, args=(circuit,))
# t4 = threading.Thread(target=voiture_4.roule_un_tour, args=(circuit,))
# t5 = threading.Thread(target=voiture_5.roule_un_tour, args=(circuit,))

# Démarrer le thread
# t.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()

# Attendre que le thread se termine
# t.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()



# for i in range(circuit.tour):
#     print(f"Tour: {i+1}")
#     for v in les_voitures:
#         v.roule_un_tour(circuit)

meilleur_temps = 1000000
voiture_gagnante = []
for v in les_voitures:
    if v.temps < meilleur_temps:
        meilleur_temps = v.temps
        voiture_gagnante = [v.marque, v.modele]

print(f"la voiture {voiture_gagnante[0]} {voiture_gagnante[1]} gagne la course avec un temps de {meilleur_temps:.2f} minutes")