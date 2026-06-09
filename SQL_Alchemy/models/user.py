
from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from profil import Profiles


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    country: Mapped[str] = mapped_column(String(50), nullable=True)

    profil: Mapped["Profiles"] = relationship(
        "Profiles",
        back_populates="user",
        uselist=False
    )

    def __repr__(self):
        return f"username = {self.username}"
    
