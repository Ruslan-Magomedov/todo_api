from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from src.database import Base


class Users(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(50))
    location: Mapped[str] = mapped_column(String(100))
    rank: Mapped[str] = mapped_column(String(10))
