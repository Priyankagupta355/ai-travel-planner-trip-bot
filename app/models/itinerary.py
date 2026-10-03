from datetime import time

from sqlalchemy import ForeignKey, Integer, Numeric, String, Time, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Itinerary(Base):
    __tablename__ = "itineraries"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    trip_id: Mapped[int] = mapped_column(
        ForeignKey("trips.id"),
        nullable=False
    )

    day_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    activity: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    location: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    start_time: Mapped[time | None] = mapped_column(
        Time,
        nullable=True
    )

    end_time: Mapped[time | None] = mapped_column(
        Time,
        nullable=True
    )

    estimated_cost: Mapped[float | None] = mapped_column(
        Numeric(10, 2),
        nullable=True
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    trip = relationship(
        "Trip",
        back_populates="itinerary_items"
    )