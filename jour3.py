
#  éviter au max les récursives (probleme de memoire)
#  penser à faire un while/for à la place

# stack heap bss

# Liste 
# ma_liste = list(1,2,3,4)
# autre_liste = [1,2,2,4]

# new_list=ma_liste.copy() # ---> créer une vraie copie (deep copy) . Si on fait un égal et qu'on modifie new_list ça modifie ma_liste
# deepcopy

# Tuple -> liste qu'on ne peut pas modifier --> lecture seule 
# mon_tuple = (1,2,3,4)
# m_tuple = 1,2,3 -> implicite

# set
# ensemble = {7,6,1,2,3,4}
# x = ensemble.pop()

# print(x)

# fruits = {"apple", "banana", "cherry"}
# x = fruits.pop() 
# print(x)


# exo 1
# import random

# aleatoire=[]
# for i in range(10):
#     aleatoire.append(random.randint(1,100))
# print(aleatoire)
# print(sum(_ for _ in aleatoire))
# print('********')

# aleatoire_2 = [random.randint(1,100) for i in range(10)]
# print(aleatoire_2)
# print(sum(_ for _ in aleatoire_2))

# exo 2
# name = input("Prénom : ")
# last_name = input("Nom : ")
# my_tuple = (name, last_name)
# print(my_tuple[0], my_tuple[1])


# exo 3
# import random

# aleatoire_1 = {random.randint(1,21) for i in range(10)}
# aleatoire_2 = {random.randint(1,21) for i in range(10)}
# print(aleatoire_1, aleatoire_2)
# x = aleatoire_1.intersection( aleatoire_2)
# print(x)
# # prof :
# exemple = set(random.sample(range(1,21)),10)

# exo 4
# mon_dico = {"banane" : 5, "pomme" : 7, "orange" : 6}
# fruit = input("fruit (banane/pomme/orange) : ")
# print(mon_dico.get(fruit))  # le get est plus safe, si clé n'existe pas ça ne plante pas
# prof :
# if fruit in mon_dico:  
# # check d'abord si c'est dedans -> du coup pas besoin du get 
# -> les crochets c'est bon




# exo 5
# ma_liste = [("Paul", 25),("Jésus", 33),("Greg", 54)]
# vieux = 0
# name = ''
# for n,v in ma_liste:
#     if v > vieux:
#         vieux = v
#         name = n
# print(f"Le plus vieux : {name}")
# # prof :
# oldest = ma_liste[0]
# for i in ma_liste:
#     if i[1] > oldest[1]:
#         oldest = i
# print(f"Le plus vieux : {oldest}")



# exo 6
# import random
# aleatoire = [random.randint(1,51) for i in range(10)]
# print(aleatoire)
# pair = [i for i in aleatoire if i % 2 == 0]
# print(pair)

#  exo 7
# doublons = ["haha", "hahu", "haha", "hihi", "hihi", "hoho"]
# elimination = list(set(doublons))
# print(elimination)

# exo 8 
# cours = { 
#             "math" : ["Paul","Greg","Rudy"],
#             "chimie" : ["Machin","Greg","Brol"],
#             "physique" : ["Vince","Alex"],
#             "gym" : ["Mister T","Hulk Hogan","Boy George"]
#         }

# cours["math"].append("Jésus")
# cours["gym"].append("Judas")
# val_cours = input("Entrez cours (math/chimie/physique/gym) : ")
# print(cours[val_cours])
# prof 
# print(', '.join(cours[val_cours]))

# exo 9 
# list_tuple = [(("pommes", 6),("banane", 10),("noix", 9)),
#               (("pommes", 2),("banane", 20),("noix", 5)),
#               (("pommes", 16),("banane", 3),("noix", 2),("fraise",15)),]
# prix = {"pommes" : 5, "banane" : 3, "noix" : 20, "fraise" : 7 }

# for k,i in enumerate(list_tuple):
#     total = 0
#     for j in i:
#         total += prix.get(j[0])*j[1]
#     print(f"commande {k+1}: {total}")

# exo 10 
# ---> oubli : pour chaque département
# list_dico = [ 
#             {"nom" : "Judith", "salaire" : 10000, "departement" : "IT" },
#             {"nom" : "Fred", "salaire" : 2000, "departement" : "RH" },
#             {"nom" : "Céline", "salaire" : 6000, "departement" : "RD" },
#             {"nom" : "Paul", "salaire" : 50000, "departement" : "Finance" },
#             ]
# salaire = 0
# nbr = 0
# for i in list_dico:
#     salaire += i["salaire"] 
#     nbr += 1 
# print(f"Moyenne : {int(salaire/nbr)}")