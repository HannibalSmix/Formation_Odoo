from sqlalchemy.orm import Session
from models.profil import Profiles
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select


def create_profil(session: Session, bio: str, user_id):
    
    profil = Profiles(bio=bio, user_id=user_id)

    try:
        session.add(profil) 
        session.commit() # envoi vers la DB
    except IntegrityError:
        session.rollback()
        print("Profil déjà existant")

    session.refresh(profil)

    return profil


def get_profil_by_userid(user_id: str, session: Session):
    stmt = select(Profiles).where(Profiles.user_id == user_id)
    profil = session.execute(stmt).scalar_one_or_none()
#   users = session.execute(stmt).scalars().all() --> pour récupérer tous les objets
    return profil