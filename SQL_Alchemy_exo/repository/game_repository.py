from sqlalchemy.orm import Session, joinedload
from models.game import EnumPegy, Games
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func, select
from datetime import datetime

from models.publisher import Publishers
from models.review import Reviews
from models.usergame import UserGames

def create_game(session: Session, title: str, price: float, release_date: datetime, pegy: EnumPegy, publisher_id : int):
    
    game = Games(title=title,
            price=price,
            release_date=release_date,
            pegy=pegy,
            publisher_id=publisher_id
        )

    try:
        session.add(game) 
        session.commit()    # envoi vers la DB
    except IntegrityError as e:
        session.rollback()
        print(f"Erreur : {e.orig}")

    session.refresh(game)

    return game 

def get_all_game(session: Session):
    stmt = select(Games).join(Games.publisher, isouter=True)
    games = session.execute(stmt).scalars().all()

    return games

def get_all_game_from_publisher(session: Session, publisher_name: str):
    # 3 ways to get publisher_id from publisher_name 

    #1 stmt = select(Publishers.id).where(Publishers.name == publisher_name)
    #1.1 publisher_id = session.execute(stmt).scalars().first()
    #1.2 publisher_id = session.execute(stmt).scalar_one_or_none()
    
    # 2
    stmt = select(Publishers).where(Publishers.name == publisher_name)
    publisher = session.execute(stmt).scalar_one_or_none()
    publisher_id = publisher.id 

    stmt = select(Games).join(Games.publisher, isouter=True).where(Games.publisher_id == publisher_id)
    games = session.execute(stmt).scalars().all()

    return games


def get_all_game_from_user(session: Session, usr_id: int):

    stmt = select(Games).join(Games.usergames, isouter=False).where(UserGames.user_id == usr_id)
    games = session.execute(stmt).scalars().all()

    return games

def get_all_game_costing_more(session: Session, price: float):

    stmt = select(Games).where(Games.price > price)
    games = session.execute(stmt).scalars().all()

    return games


def display_average_rating_per_game(session: Session):

    stmt = select(Games.title, func.avg(Reviews.rating)).join(Reviews, Games.id == Reviews.game_id).group_by(Games.id)
    results = session.execute(stmt).all()

    for title, avg_rating in results:
        print(f"Jeu : {title}, Note moyenne : {avg_rating:.2f}")


def display_top_5_most_purchased_games(session: Session):

    stmt = select(Games.title, func.count(UserGames.game_id)).join(UserGames, Games.id == UserGames.game_id).group_by(Games.id).order_by(func.count(UserGames.game_id).desc()).limit(5)
    results = session.execute(stmt).all()

    for title, purchase_count in results:
        print(f"Jeu : {title}, Nombre d'achats : {purchase_count}")

def display_all_games_with_total_players_total_hours_played(session: Session):

    stmt = select(Games.title, func.count(UserGames.user_id), func.sum(UserGames.hours_played)).join(UserGames, Games.id == UserGames.game_id).group_by(Games.id)
    results = session.execute(stmt).all()

    for title, total_players, total_hours in results:
        print(f"Jeu : {title}, Total de joueurs : {total_players}, Total d'heures jouées : {total_hours}")