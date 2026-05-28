# faire attention aux import -> depuis le fichier d'execution

# stopIteration -> fin boucle for
# tjrs mettre qqchose dans except xxxError: -> pas de pass

# try:
# except xxxerror:
#  ne jamais envoyer les msg d'erreur de SQL -> mine d'or pour les hackers
# finally: s'exécute que le code ait réussi ou non (except)
# raise -> renvoie quand même l'erreur (de base)

# with -> bonne façon de faire car il va gérer fermeture dans tous les cas
# ->ouverture fichier, ou DB
# peut mettre un try except dans un with
 
# page 115 erreur dans le slide, il n'y aura pas d'erreur dans le 3eme cas

#  peut mettre un tuple comme type d'except : p 118
# traceback -> trace les erreurs jusqu'à l'origine
# traceback.print_exc() -> pour debug c'est bien et 
# pour prod faut faire attention à ce qu'on envoie

# Check les ORM -> securiser injection url, corerule github, 
# modesecurity-crs (owasp)
# sanitize la string, éviter la concaténation

# dbeaver -> to check pour semaine prochaine
# ou DataGrip
# vs code plugin -> database client JDBC