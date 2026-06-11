from sqlalchemy.orm import Session, joinedload
from models.publisher import Publishers
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, func
from datetime import datetime
from models.game import Games

def get_all_publisher(session: Session):
    """
    Afficher tous les publishers.
    """
    stmt = select(Publishers)
    publishers = session.execute(stmt).scalars().all()

    return publishers

def display_all_publishers_with_total_games_average_game_price(session: Session):

    stmt = select(Publishers.name, func.count(Games.id), func.avg(Games.price)).join(Games, Games.publisher_id == Publishers.id, isouter=True).group_by(Publishers.id)
    results = session.execute(stmt).all()

    for publisher_name, total_games, avg_price in results:
        print(f"Publisher : {publisher_name}, Total de jeux : {total_games}, Prix moyen des jeux : {avg_price:.2f}")