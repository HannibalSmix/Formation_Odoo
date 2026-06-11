from sqlalchemy.orm import Session, joinedload
from models.usergame import UserGames
from models.user import Users
from models.game import Games
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func, select
from datetime import datetime

def buy_game(session: Session, usr_id: int, game_id: int):
    
    user = session.get(Users, usr_id)
    game = session.get(Games, game_id)
    user_age = datetime.now().year - user.bod.year if user else None
    game_pegy = game.pegy.value if game else None
    if user_age < game_pegy:
        print(f"L'utilisateur avec id {usr_id} n'est pas autorisé à acheter le jeu avec id {game_id}.")
        return None
    else:

        user_game = UserGames(
            user_id=usr_id,
            game_id=game_id,
            purchase_date=datetime.now()
        )

        try:
            session.add(user_game)
            session.commit()
        except IntegrityError as e:
            session.rollback()
            print(f"Erreur : {e.orig}")

        session.refresh(user_game)

        return user_game


def play_game(session: Session, usr_id: int, game_id: int, hours: int):
    
    if hours < 0:
        print("Le nombre d'heures jouées ne peut pas être négatif.")
        return None

    user_game = session.get(UserGames, (usr_id, game_id))
    if user_game:
        user_game.hours_played = (user_game.hours_played or 0) + hours
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Erreur : {e}")
        return user_game
    
    else:
        print(f"Aucun achat trouvé pour l'utilisateur {usr_id} et le jeu {game_id}.")
        return None
    
def refund_game(session: Session, usr_id: int, game_id: int):
    user_game = session.get(UserGames, (usr_id, game_id))
    if user_game:
        session.delete(user_game)
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Erreur : {e}")
            return False
        print(f"Le remboursement pour l'utilisateur {usr_id} et le jeu {game_id} a été effectué avec succès.")
        return True
    else:
        print(f"Aucun achat trouvé pour l'utilisateur {usr_id} et le jeu {game_id}.")
        return False
    
def display_number_of_pruchase_per_game(session: Session):
    
    stmt = select(Games.title, func.count(UserGames.game_id)).join(UserGames, Games.id == UserGames.game_id).group_by(Games.id)
    results = session.execute(stmt).all()
    
    for title, count in results:
        print(f"Le jeu '{title}' a été acheté {count} fois.")