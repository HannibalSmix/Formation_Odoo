from db.database import Base, engine
from sqlalchemy.orm import sessionmaker
from models.user import Users
from models.usergame import UserGames
from models.review import Reviews
from models.publisher import Publishers
from models.gender import Genders
from models.game import Games

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

with SessionLocal() as session:
    
    print('hello')