from typing import Annotated

from fastapi import FastAPI, Query, Depends

from src.models import BookingSchemas, SearchSchema

from src.booking.router import router as router_bookings
from src.users.router import router as router_users

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)


@app.get("/hotels")
def get_hotels(
    params: Annotated[SearchSchema, Depends(SearchSchema)]
):

    return SearchSchema


@app.post("/booking")
def add_booking(
    booking: BookingSchemas,
):
    pass