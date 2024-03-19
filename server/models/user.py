from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class User(Base, UserMixin):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
