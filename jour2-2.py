# les preuves de programme --> le delta de la condition de sortie doit diminuer strictement

# O(n) -> au pire des cas le nb boucle
#  tri fusion -> c'est un tri en recursif
# les di
# dictionnaires sont implémentées en RBT

# import math

# for i in range(2,101):
#     is_premier = True
#     for j in range(2,int(math.sqrt(i))+1):
#         if i % j == 0:
#             is_premier = False
#             break
#     if is_premier:
#         print(i, end=" est premier\n")
        
# exo 2

# age = int(input("Entrez l'age: "))
# majeur_mineur = "Utilisateur mineur" if age < 18 else "Utilisateur majeur"
# print(majeur_mineur)

# réponse formateur :
# print('Vous pouvez entrer' if int(input('Age : ')) >= 18 else "Vous ne pouvez pas entrer")


# import random

# exo 3
# number = random.randint(1,100)
# count = 0
# encore = True
# while encore:
#     guess = int(input("Entrez un nombre: "))
#     if guess == number:
#         encore = False
#         print("Vous avez trouvé !!")
#     else:
#         if guess > number:
#             print("trop grand")
#         else:
#             print("trop petit") 
#         chercher_encore=input("Voulez vous continuer (o-n) ?")
#         if chercher_encore == 'n':
#             encore = False


def confirm_input(prompt):
    response = input(prompt + "y/Y")
    if response in ['y','Y']:
        return True
    return False

confirm = confirm_input("Voulez-vous conti") if not confirm else False

# mot=input("entrez un mot: ")
# for i in mot:
#     print(i)


#  challenge:  Allée 2 metres de large, n de long. dalle 1m sur 2m et les dalles sont de 2 couleurs
# combien de possibilité de recouvrement y a t'il en fction de n?
# n = 2
# count = 0
# def carreler(n, count) -> int:
#     if n == 0:
#         return 1
#     elif n < 0:
#         return 0
#     else:
#         count += carreler(n-1, count)
#         count += carreler(n-1, count)

#         count += carreler(n-2, count)
#         count += carreler(n-2, count)
#         count += carreler(n-2, count) 
#         count += carreler(n-2, count)
#         return count
#     # soit 1 à la verticale -> progresse de 1 m
#     # soit 2 à l'horizontale -> progresse de 2 m

# c=carreler(n,count)
# print(c)

