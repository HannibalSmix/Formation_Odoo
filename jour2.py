print('hello')

a="blop"
b="blop"

print(a==b)

a+="biblop"
b+="biblop"

print(a==b) # le double = compare la stack --> faut implementer __eq__() pour comparer la heel
# tout est objet en python --> pour le int tout a été surcharger pour qu'il ait un comportement primitif
  
#   le and est prioritaire sur le ou : a and b or c  -> le et est une multiplication et le ou est une addition
#   qd compare avec un and commencer par celle qui a le plus de probabilité d'etre nulle
#   pas de cascade dans match valeur: 
#       case 1:
#       case 2:

# taille = input('Taille du café (s, m ou l) : ')
# _type = input('Type du café (lait, froid, classique): ')
# extra = input('Extra (chocolat, mousse): ')
# cout = 0

# match taille:
#     case 's': cout+=3
#     case 'm': cout+=5
#     case 'l': cout+=7
#     case _: pass
# match _type:
#     case 'lait': cout+=4
#     case 'froid': cout+=6
#     case 'classique': cout+=3
#     case _: cout+=0

# match extra:
#     case 'chocolat': cout+=2
#     case 'mousse': cout+=1
#     case _: cout+=0

# print(f"Prix du café: {cout}")


# note_numerique=int(input("Note numérique (1-10) : "))
# note_alpha=''
# match note_numerique:
#     case 1 | 2 | 3 | 4 | 5:
#         note_alpha='F'
#     case 6:
#         note_alpha='E'
#     case 7:
#         note_alpha='D'
#     case 8:
#         note_alpha='C'
#     case 9:
#         note_alpha='B'
#     case 10:
#         note_alpha='A'
# print("Note Alpha: " + note_alpha)


# import random
# random_int = random.randint(1, 10)
# valeur = int(input("Entrez valeur : "))
# if valeur == random_int:
#     print("Bravo trouvé")
# elif valeur < random_int:
#     valeur = int(input("Trop petit. Réessaye"))
# else:
#     valeur = int(input("Trop grand. Réessaye"))

# if valeur == random_int:
#     print("Bravo trouvé")
# elif valeur < random_int:
#     valeur = int(input("Trop petit. Réessaye"))
# else:
#     valeur = int(input("Trop grand. Réessaye"))

# if valeur == random_int:
#     print("Bravo trouvé")
# else:
#     print("Raté dommage")

# taille=int(input("Taille (cm): "))
# poids=int(input("Poids: "))
# icm = 10000*poids/(taille*taille)
# if icm >= 25:
#     print(f"surpoids: {icm:.2f}")
# elif icm < 25 and icm >= 18.5:
#     print(f"parfait: {icm:.2f}")
# else:
#     print(f"Manque de poids: {icm:.2f}")

# menu_petit_dej =int(input('Choisissez menu pour petit-dej (1-2-3)'))
# menu_dej =int(input('Choisissez menu pour dej (1-2-3)'))
# menu_diner =int(input('Choisissez menu pour diner (1-2-3)'))
# print(menu_petit_dej, menu_dej, menu_diner, sep="--")


# import random

# nombre_aleatoire = random.randint(1, 3)
# citation1 = ''
# citation2 = ''
# citation3 = ''
# match nombre_aleatoire:
#     case 1:
#         citation1 = 'Citation A1'
#         citation2 = 'Citation A2'
#         citation3 = 'Citation A3'
#     case 2:
#         citation1 = 'Citation B1'
#         citation2 = 'Citation B2'
#         citation3 = 'Citation B3'
#     case 3:
#         citation1 = 'Citation C1'
#         citation2 = 'Citation C2'
#         citation3 = 'Citation C3'
    
# theme = int(input("Entrez un theme (1,2,3): "))
# match theme:
#     case 1:
#         print(citation1)
#     case 2:
#         print(citation2)
#     case 3:
#         print(citation3)
#     case _:
#         print("pas de theme")


