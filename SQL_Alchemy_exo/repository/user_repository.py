from sqlalchemy.orm import Session, joinedload
from models.user import Users
from models.gender import MyEnum
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from datetime import datetime
import enum

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
