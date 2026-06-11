from sqlalchemy.orm import Session, joinedload
from models.review import Reviews
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func, select

def review_game(session: Session, user_id: int, game_id: int, rating: int, comment: str):

    if rating < 0 or rating > 5:
        print("La note doit être comprise entre 0 et 5.")
        return None

    review = Reviews(
        user_id=user_id,
        game_id=game_id,
        rating=rating,
        comment=comment
    )

    try:
        session.add(review)
        session.commit()
    except IntegrityError as e:
        session.rollback()
        print(f"Erreur : {e.orig}")
        return None

    session.refresh(review)

    return review

def get_all_reviews_from_game(session: Session, game_id: int):

    stmt = select(Reviews).join(Reviews.game, isouter=True).where(Reviews.game_id == game_id)
    reviews = session.execute(stmt).scalars().all()

    return reviews
