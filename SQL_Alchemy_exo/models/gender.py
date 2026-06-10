from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Identity
from typing import TYPE_CHECKING
import enum
from sqlalchemy import Enum

if TYPE_CHECKING:
    from user import Users
#     from post import Posts


class MyEnum(enum.Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3


class Genders(Base):
    __tablename__ = "genders"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)  #identity pour GENERATED ALWAYS AS IDENTITY
    gender: Mapped[str] = mapped_column(Enum(MyEnum))

    user: Mapped["Users"] = relationship(
        "Users",
        back_populates="gender",
        uselist=False   
    )

    def __repr__(self):
        return f"username = {self.username}, email = {self.email}, gender = {self.gender}"
    
