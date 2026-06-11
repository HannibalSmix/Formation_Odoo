from sqlalchemy.orm import Session, joinedload
from models.post import Posts
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select


def create_post(session: Session, post: str, usr_id: int):
    
    post = Posts(post=post, usr_id=usr_id)

    try:
        session.add(post) 
        session.commit()  # envoi vers la DB
    except IntegrityError:
        session.rollback()
        print("Erreur création post")

    session.refresh(post)

    return post