from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


from app.database.base import Base


class Trip(Base):
    __tablename__ = "trips"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    destination: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    end_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    budget: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    travelers: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    trip_type: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="planned",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="trips"
    )

    itinerary_items = relationship(
        "Itinerary",
        back_populates="trip",
        cascade="all, delete-orphan"
    )

    conversations = relationship(
        "Conversation",
        back_populates="trip",
        cascade="all, delete-orphan"
    )   