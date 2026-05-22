# différence entre fction et procédure
# procédure -> ne retourne rien
# fonction -> retourne une valeur

# def pour_plusieurs_args(*args):
#     print(args)

# def pour_kwargs(**kwargs): #passe un ensemble de clés valeurs
#     print(kwargs)

# pour_kwargs(uneclé="unevaleur", unedeuxiemeclé="unedeuxiemevaleur", unetroisiemeclé="unetroisiemevaleur")

# def fction(a,b,c):
#     pass

# fction(b=3,a=8,c=10) # -> dans ce cas là, les variables peuvent être mis dans un autre ordre

# quand on met le typage, ça aide pour l'autocomplétion 
# def exemple(a: int, b: list[int]) -> dict[str, list[int]]:  -> idem pour la valeur de retour
#  idealement une fonction max 15 lignes -> ça arrive que plus long mais ça doit être rare

# def modifstring(modif):
#     modif = "abc"

# mod="aaaaaa"
# modifstring(mod)
# print(mod)
# ---------------------------------------------------------------
# ---------------------------------------------------------------
# ---------------------------------------------------------------

# # exo 1
# def calcul_moyenne(notes: list[int]) -> float:
#     if len(notes) == 0:
#         return 0.0

#     total = sum(i for i in notes)
#     return total/len(notes)

# print(calcul_moyenne([1,2,3,4,6,5,7]))


# # exo 2
# def recherche_min(notes: list[int]) -> float:
#     return min(notes)

# print(recherche_min([1,2,3,4,6,5,7]))

# # exo 3
# def generer_email(*args, domain="hulkhogan.us") -> str:
#     #return f"{prenom}.{nom}@{domain}"
#     return '.'.join(args) + '@' + domain

# print(generer_email("Et","Vw"))

# #exo 4
# def compte_mots(phrase):
#     ph=phrase.replace('.','').replace(',', '').replace(';', '').replace('\'', '').replace('?', '')
#     print(ph)
#     s=ph.strip().split(' ')
#     print(s)
#     return len(s)
# print(compte_mots("Voici une phrase de ouf, top. Et ça marche ?"))

#  prof
# import re
# def count_words(sentence: str) -> int:
#     word_count = {}
#     words = re.split(r"[\s']+", sentence) # le + pour enlever les répétitions

#     return len(words)
# print(count_words("Voici une phrase d'ouf,      top. Et ça marche?"))

# # exo 5
# def convertir_temperature(celsius):
#     return (celsius*9/5)+32

# print(convertir_temperature(1))

# # exo 6 
# def nombres_pairs_impairs(nbres):
#     pairs = []
#     impairs = []
#     for i in nbres:
#         if i % 2 == 0:
#             pairs.append(i)
#         else:
#             impairs.append(i)
#     return pairs, impairs

# print(nombres_pairs_impairs([1,5,9,7,6,3,4]))

# exo 7
# def inverser_chaine(chaine):
#     return chaine[::-1]
# print(inverser_chaine("abcdef")) 

# exo 8
# import re
# def valider_mot_de_passe(password):
#     valid = True
#     if len(password) < 8:
#         valid = False
#     if re.search(r"[a-z]", password) is None:
#         valid = False
#     if re.search(r"[A-Z]", password) is None:
#         valid = False
#     if re.search(r"[@#$%&_-]", password) is None:
#         valid = False
#     if re.search(r"[0-9]", password) is None:
#         valid = False
#     return valid
# print(valider_mot_de_passe("az9L-zzzzzz"))

# prof  ---> regexr.com
# import re
# def valider_mot_de_passe(password):
#     valid = True
#     if len(password) < 8:
#         valid = False
#     if not re.match(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$", password):
#         valid = False
#     return valid
# print(valider_mot_de_passe("az9L-zzzzzz"))

