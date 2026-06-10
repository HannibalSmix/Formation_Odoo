from db.database import Base, engine
from sqlalchemy.orm import sessionmaker
from models.user import Users
from models.usergame import UserGames
from models.review import Reviews
from models.publisher import Publishers
from models.gender import Genders, MyEnum
from models.game import EnumPegy, Games
from repository.user_repository import create_user
from repository.game_repository import create_game
from datetime import datetime


Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

with SessionLocal() as session:
    
    print('hello')
    # user = create_user(session, "john_doe", "john@example.com", "USA", datetime(1990, 1, 1), MyEnum.MALE.value)
    game = create_game(session, "The Legend of Zelda: Breath of the Wild", 59.99, datetime(2017, 3, 3), EnumPegy.PEGI_12, 1)
    # print(user)
    print(game)