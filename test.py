# print('hello') 
# # interpolation de chaine de charactere
# nom : str = "Paul" 
# v : str = f"prenom {nom}"
# prenom : str | None = None # peut prendre soit un string soit un None
# print(v)
# if type(nom) is str:
#     print('nom = string')

# a,b=5,7 # on ne peut pas a: int, b: int = 5, 7
# print(f"A={a} et B={b}")
# b,a=a,b
# print(f"A={a} et B={b}")

# nom_prenom=input("Quel est ton prénom et nom ?")
# splitter=nom_prenom.split(" ")
# print(f"tu t'appelles : {splitter[0]}", splitter[1], sep = ":-)")

# # def strtoint(data: str) -> int:

# print("Salut", end=":)")
# print("tu", end="-")
# print("vas", end="#")
# print("bien", end="?\n")

# print("Salut", "tu", "vas", "bien", sep=":-)\n", end=":)\n")


# mot_1=input("1er mot ? ")
# mot_2=input("2eme mot ? ")
# print(f"{mot_1}{mot_2}")
# print(mot_1 + mot_2)


# nb_1=int(input("1er nombre ? "))
# nb_2=int(input("2eme nombre ? "))
# print(f"Somme = {nb_1+nb_2} ", end=":):):)")

# print(3,6,9,sep=":-)", end="@@@@")

# a=12
# b=3*a+8 # 44
# c=b-2*a # 20
# d=(c+25)*b # 1980
# e=(a+b)%10 # 6
# f=(c*d)//(b+6) # 39600 // 50  = 792
# g=(d+e)//(f-9) # 1986 // 783 = 2

# print(a, b, c, d, e, f, g)

# a=13
# b=5
# c=True
# d=not(c)

# print(a>10 and b<20) # True
# print(c != 40 or d >= 100) # True  -> le True est transformé en 1
# print(a==2 and not(b>15)) # False
# print(c>50 or not(d<200)) # True-> False !! --> false est transformé en 0
# print((a<b and c>30) or (d==270)) # False
# print(not(a*b>100)) # True
# print(b==15 or (c>60 and a<5)) # False
# print(((b==15 or (c>60 and a<5)) and (a<b)) or not(b==9)) # True

def convertion(sec):
    seconde = sec%60
    t = sec//60
    min = t%60
    t = t//60
    heure = t%60
    t = t//60
    jour = t%24
    print(jour, "jours", heure, "heures", min, "minutes", seconde, "secondes")

    d_min= sec//60
    d_hours= d_min//60
    d_days = d_hours//24

    d_hours = d_days%24
    d_min = d_hours%60
    d_sec = d_min%60

    print(d_days,d_hours,d_min,d_sec)

convertion(4561)

# la stack & la heep  

# def inversion():
#     a=10
#     b=30
#     a=a+b
#     b=a-b
#     a=b-a
#     print(a, b)