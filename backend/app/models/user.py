from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

class User(Base):
    __tablename__ = 'users'

    id:Mapped[int] = mapped_column(primary_key=True)
    email:Mapped[str] = mapped_column(String(30))
    name:Mapped[str] = mapped_column(String(30))
    password:Mapped[str] = mapped_column(String(100))
