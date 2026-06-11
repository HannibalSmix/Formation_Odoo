from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Identity, ForeignKey, Float, DateTime
from typing import TYPE_CHECKING
from datetime import datetime
import enum
from sqlalchemy import Enum
from sqlalchemy import CheckConstraint

from models.review import Reviews
from models.usergame import UserGames

if TYPE_CHECKING:
    from publisher import Publishers
#     from post import Posts



class EnumPegy(enum.Enum):
    PEGI_3 = 1
    PEGI_7 = 7
    PEGI_12 = 12
    PEGI_16 = 16
    PEGI_18 = 18

class Games(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True) #identity pour GENERATED ALWAYS AS IDENTITY
    title: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=True)
    release_date: Mapped[datetime] = mapped_column(DateTime)
    pegy: Mapped[str] = mapped_column(Enum(EnumPegy))

    publisher_id: Mapped[int] = mapped_column(ForeignKey("publishers.id"))
    publisher: Mapped["Publishers"] = relationship(
        "Publishers",
        back_populates="game",
        uselist=False
    )
    usergames: Mapped["UserGames"] = relationship(
        "UserGames",
        back_populates="game"
    )

    reviews: Mapped["Reviews"] = relationship(
        "Reviews",
        back_populates="game"
    )    

    __table_args__ = (
        CheckConstraint('price >= 0', name='check_price_non_negative'),
    )

    def __repr__(self):
        return f"id = {self.id}, title = {self.title}, price = {self.price}, release_date = {self.release_date}, pegy = {self.pegy}"
    
