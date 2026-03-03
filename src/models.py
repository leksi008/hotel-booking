from datetime import date

from fastapi import Query
from pydantic import BaseModel


class BookingSchemas(BaseModel):
    room_id: int
    date_from: date
    date_to: date


class SearchSchema(BaseModel):
    location: str
    date_to: str | None = None
    date_from: int | None = Query(None, ge=1, le=10)