from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Identity, ForeignKey
from typing import TYPE_CHECKING
from sqlalchemy import DateTime
from sqlalchemy import CheckConstraint
from datetime import datetime
from sqlalchemy import Integer

if TYPE_CHECKING:
    from game import Games
    from user import Users


class UserGames(Base):
    __tablename__ = "usergames"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"), primary_key=True) #identity pour GENERATED ALWAYS AS IDENTITY
    purchase_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    hours_played: Mapped[int] = mapped_column(Integer, nullable=True, default=None)

    user: Mapped["Users"] = relationship(
        "Users",
        back_populates="usergames",
        uselist=False
    )
    game: Mapped["Games"] = relationship(
        "Games",
        back_populates="usergames",
        uselist=False
    )


    __table_args__ = (
        CheckConstraint('hours_played >= 0', name='hours_played_non_negative'),
    )

    def __repr__(self):
        return f"user_id = {self.user_id}, game_id = {self.game_id}, purchase_date = {self.purchase_date}, hours_played = {self.hours_played}"
    
