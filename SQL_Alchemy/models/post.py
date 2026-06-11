
from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Identity, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from user import Users


class Posts(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True) #identity pour GENERATED ALWAYS AS IDENTITY
    post: Mapped[str] = mapped_column(String(500), unique=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["Users"] = relationship(
        "Users",
        back_populates="post"
    )

    def __repr__(self):
        return f"post = {self.post}"
    
