from sqlalchemy.orm import Session, joinedload
from models.game import Games
from models.user import Users
from models.gender import MyEnum
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func, select
from datetime import datetime
import enum

from models.usergame import UserGames

def create_user(session: Session, username: str, email: str, country: str, bod: datetime, gender: MyEnum):
    
    user = Users(username=username,
            email=email,
            country=country,
            bod=bod,
            gender_id=gender
        )

    try:
        session.add(user) 
        session.commit()    # envoi vers la DB
    except IntegrityError:
        session.rollback()
        print("Utilisateur déjà existant")

    session.refresh(user)

    return user


def get_all_user(session: Session):
    """
    Afficher tous les utilisateurs avec leur profil.
    """
    stmt = select(Users).join(Users.gender_rel, isouter=True)
    users = session.execute(stmt).scalars().all()

    return users

def get_all_user_own_games_more_than(session: Session, min_games: int):

    stmt = select(Users).join(Users.usergames, isouter=True).group_by(Users.id).having(func.count(UserGames.game_id) > min_games)
    users = session.execute(stmt).scalars().all()

    return users


def display_top_5_users_with_most_total_hours_played(session: Session):

    stmt = select(Users.username, func.sum(UserGames.hours_played)).join(UserGames, UserGames.user_id == Users.id).group_by(Users.id).order_by(func.sum(UserGames.hours_played).desc()).limit(5)
    results = session.execute(stmt).all()

    for username, total_hours in results:
        print(f"Utilisateur : {username}, Total d'heures jouées : {total_hours}")

def display_all_user_games_owned_hours_played(session: Session):

    stmt = select(Users.username, func.count(Games.title), func.sum(UserGames.hours_played)).join(UserGames, UserGames.user_id == Users.id).join(Games, UserGames.game_id == Games.id).group_by(Users.id)
    results = session.execute(stmt).all()

    for username, total_games, total_hours in results:
        print(f"Utilisateur : {username}, Total de jeux possédés : {total_games}, Total d'heures jouées : {total_hours}")
