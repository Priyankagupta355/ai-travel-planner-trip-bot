from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Preference(Base):
    __tablename__ = "preferences"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    food_preference: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    travel_style: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    favorite_activities: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    budget_preference: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    user = relationship(
        "User",
        back_populates="preference"
    )