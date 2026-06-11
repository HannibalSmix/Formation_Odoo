from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Identity
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from user import Users


class Profiles(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    bio: Mapped[str] = mapped_column(String(500))
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    user: Mapped["Users"] = relationship(
        "Users",
        back_populates="profil" #   relie les deux côtés de la relation.
    )
    
    
    def __repr__(self):
        return f"bio = {self.bio}"