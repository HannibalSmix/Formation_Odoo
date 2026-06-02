from dataclasses import dataclass

class Human:
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies

    # def __eq__(self, other: "Human"):
    #     return self.name == other.name

    def __gt__(self, other: "Human"):
        return self.age > other.age
    
    def __ge__(self, other: "Human"):
        return self.age >= other.age
    
    def __contains__(self, items):
        return items in self.hobbies
    
    def __getitem__(self, key):
        return self.hobbies[key]
    
@dataclass  # sert qu'à stocker des données, pas de méthode
class Position:
    x: int
    y: int #field(compare=False) --> permet de ne pas comparer cet attribut
    ch: str

pos1 = Position(5, 5, 'pol')
pos2 = Position(5, 5, 'pol')
print([pos1])
print(pos1 == pos2)

hum1 = Human('pol', 18, ['music', 'chess'])
hum2 = Human('pol', 18, ['music', 'chess'])

print("égal? ", hum1 == hum2)
print(hum1 > hum2)

print('music' in hum1)
print(hum1[1])