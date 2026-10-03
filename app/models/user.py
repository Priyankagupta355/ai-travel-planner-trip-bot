from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(100), nullable=False)

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )


    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    trips = relationship(
        "Trip",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    conversations = relationship(
        "Conversation",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    preference = relationship(
        "Preference",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )