from db.database import Base, engine
from sqlalchemy.orm import sessionmaker
from models import gender, user, publisher, game, review, usergame 
from sqlalchemy import text


def seed():

    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    
    with SessionLocal() as session:
        with open('seed/seed.sql', 'r') as file:
            sql_statements = file.read()
        
        for statement in sql_statements.split(';'):
            if statement.strip():
                session.execute(text(statement))
        
        session.commit()
        print("✅ Seed terminé !")

if __name__ == "__main__":
    seed()
