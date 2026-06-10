from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Identity, ForeignKey
from typing import TYPE_CHECKING
from sqlalchemy import CheckConstraint, UniqueConstraint, Integer
if TYPE_CHECKING:
    from game import Games
    from user import Users


class Reviews(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True) #identity pour GENERATED ALWAYS AS IDENTITY
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"), nullable=False) #identity pour GENERATED ALWAYS AS IDENTITY
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    comment: Mapped[str] = mapped_column(String(500), nullable=True)

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
        UniqueConstraint('user_id', 'game_id', name='uq_user_game_review'),
    )

    def __repr__(self):
        return f"id = {self.id}, user_id = {self.user_id}, game_id = {self.game_id} , rating = {self.rating}, comment = {self.comment}"
    
