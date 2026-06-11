
from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Identity
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from profil import Profiles
    from post import Posts


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True) #identity pour GENERATED ALWAYS AS IDENTITY
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    country: Mapped[str] = mapped_column(String(50), nullable=True)
    favorite_food: Mapped[str] = mapped_column() # tention bug nullabe

    profil: Mapped["Profiles"] = relationship(
        "Profiles",
        back_populates="user",
        uselist=False
    )
    post: Mapped["Posts"] = relationship(
        "Posts",
        back_populates="user"
    )

    def __repr__(self):
        # checker inspect -> : state = inspect(self) # pour check s'il y a un profil
        return f"username = {self.username}, email = {self.email}, country = {self.country}"
    
