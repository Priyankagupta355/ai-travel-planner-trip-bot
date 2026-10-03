from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field, model_validator


class TripCreate(BaseModel):
    destination: str = Field(min_length=2, max_length=100)
    start_date: date
    end_date: date
    budget: Decimal = Field(gt=0)
    travelers: int = Field(gt=0)
    trip_type: str = Field(min_length=2, max_length=50)

    @model_validator(mode="after")
    def validate_dates(self):
        if self.end_date < self.start_date:
            raise ValueError("End date cannot be before start date")
        return self


class TripUpdate(BaseModel):
    destination: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )
    start_date: date | None = None
    end_date: date | None = None
    budget: Decimal | None = Field(default=None, gt=0)
    travelers: int | None = Field(default=None, gt=0)
    trip_type: str | None = Field(
        default=None,
        min_length=2,
        max_length=50
    )
    status: str | None = None


class TripResponse(BaseModel):
    id: int
    user_id: int
    destination: str
    start_date: date
    end_date: date
    budget: Decimal
    travelers: int
    trip_type: str
    status: str

    model_config = {
        "from_attributes": True
    }