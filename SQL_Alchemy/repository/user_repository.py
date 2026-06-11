from sqlalchemy.orm import Session, joinedload
from models.user import Users
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select

def create_user(session: Session, username: str, email: str, country: str):
    
    user = Users(username=username, email=email, country=country)

    try:
        session.add(user) 
        session.commit() # envoi vers la DB
    except IntegrityError:
        session.rollback()
        print("Utilisateur déjà existant")

    session.refresh(user)

    return user


def get_user_by_username(username: str, session: Session):
    stmt = select(Users).where(Users.username == username)
    user = session.execute(stmt).scalar_one_or_none()
#   users = session.execute(stmt).scalars().all() --> pour récupérer tous les objets
    return user


def get_user_by_id(id: int, session: Session):
    stmt = select(Users).where(Users.id == id)
    user = session.execute(stmt).scalar_one_or_none()
#   users = session.execute(stmt).scalars().all() --> pour récupérer tous les objets
    return user


def get_all_user(session: Session):
    """
    Afficher tous les utilisateurs avec leur profil.
    """
    stmt = select(Users).join(Users.profil, isouter=True)
    users = session.execute(stmt).scalars().all()

    return users


def get_by_username_w_profil_join(username: str, session: Session):
    stmt = select(Users).option(joinedload(Users.profil)).where(Users.username == username)
    user = session.execute(stmt).scalar_one_or_none()
    return user


def update_user_email(session: Session, user_id: int, new_email: str):
    stmt = select(Users).where(Users.id == user_id)
    user = session.execute(stmt).scalar_one_or_none()

    if user is None:
        return None

    user.email = new_email
    session.commit()
    session.refresh(user)

    return user


def update_user_country(session: Session, user_id: int, new_country: str):
    stmt = select(Users).where(Users.id == user_id)
    user = session.execute(stmt).scalar_one_or_none()

    if user is None:
        return None

    user.country = new_country
    session.commit()
    session.refresh(user)

    return user


def delete_user(session: Session, user_id: int):
    stmt = select(Users).where(Users.id == user_id)
    user = session.execute(stmt).scalar_one_or_none()

    if user is None:
        return False

    try:
        session.delete(user)
    except IntegrityError:
        print("User doesn't exist")
        return False
    
    session.commit()

    return True

