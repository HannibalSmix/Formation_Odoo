from random import randint

# from typing import TYPE_CHECKING   ---> pour éviter qu'il y ait des imports circulaires
# if TYPE_CHECKING: 
#     from xxx import yyyy     ---> permettra aussi de faire le typage et avoir l'autocompletion
 
class De:
    def __init__(self, max: int = 6):
        self.__minimum = 1
        self.__maximum = max  
       
        #self.maximum = max # ici on appelle les setter (ce ne sont pas les variables)
    
    # faire les getter
    @property
    def minimum(self):
        return self.__minimum
    
    # dans l'exo on ne doit pas mettre de setter
    # @minimum.setter
    # def minmum(self, value):
    #     self.__minimum = value

    @property
    def maximum(self):
        return self.__maximum
    
    # @maximum.setter
    # def maximum(self, value):
    #     self.__maximum = value

    def lancer(self):
        return randint(self.minimum, self.maximum)
    
    def roll_best_3_of_x(self, x: int):
        rolls = [self.lancer() for _ in range(x)]
        rolls = rolls.remove(min(rolls))
        return sum(rolls)