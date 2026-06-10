from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Identity, ForeignKey, DateTime
from typing import TYPE_CHECKING
from datetime import datetime


if TYPE_CHECKING:
    from gender import Genders
#     from post import Posts


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)  #identity pour GENERATED ALWAYS AS IDENTITY
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    
    country: Mapped[str] = mapped_column(String(50))
    bod: Mapped[datetime] = mapped_column(DateTime)

    gender_id: Mapped[int] = mapped_column(ForeignKey("genders.id"))
    gender: Mapped["Genders"] = relationship(
        "Genders",
        back_populates="user"
    )

    def __repr__(self):
        return f"username = {self.username}, email = {self.email}"#, gender = {self.gender}"
    
