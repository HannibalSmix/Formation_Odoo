from db.database import Base, engine
from sqlalchemy.orm import sessionmaker
from models.user import Users
from models.profil import Profiles
from models.post import Posts
from repository.user_repository import create_user, get_user_by_username
from repository.user_repository import get_user_by_id, delete_user, get_all_user
from sqlalchemy import select


Base.metadata.create_all(engine)    # demande à SQLAlchemy de créer ces tables dans la base.

SessionLocal = sessionmaker(bind=engine)

with SessionLocal() as session:

    # user = create_user(session, "Haha", "hoho@gmail.com", "Belgium")

    user2 = get_user_by_username("Haha", session)
    print(f"EMAIL: {user2.email}")

    user3 = get_user_by_id(user2.id, session)
    print(f"EMAIL: {user3.email}, USERNAME: {user3.username}")

    # if delete_user(session, 1):
    #     print('user deleted')
    # else:
    #     print('user not deleted')

    users = get_all_user(session)
    for usr in users:
        print(usr)
        print(usr.profil)
        print()