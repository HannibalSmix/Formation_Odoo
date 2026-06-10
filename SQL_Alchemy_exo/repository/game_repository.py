from sqlalchemy.orm import Session, joinedload
from models.game import EnumPegy, Games
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from datetime import datetime

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
    except IntegrityError:
        session.rollback()
        print("Jeu déjà existant")

    session.refresh(game)

    return game 
