# # Orienté objet 

# un état 
# un comportement

# Entre fichier
# from Package.Fichier import ma_fonction

# Le fichier d'execution doit soit trouver à la racine

# if __name__ == "__main__":
#     print('hello woooorld')

# un fichier s'execute au moment de l'import.
# si on veut faire des test dans un fichier import on peut mettre if __name__ == "__main__":
# on peut executer le code dans le if si on execute bien le fichier à importer.

# nommage des classes : PascalCase (majuscule à chaque mot)

class Voiture:
    def __init__(self):
        self.__roues = 4 # les __ rendent la variable privée

    @property
    def roues(self):
        return self.__roues

    @roues.setter  
    def roues(self, value):
        self.__roues = value


ma_voiture = Voiture()
ma_voiture.roues = 5   # sans le mutateur (setter) on ne pourrait pas modifier roues
print(ma_voiture.roues)