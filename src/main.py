from typing import Annotated

from fastapi import FastAPI, Query, Depends

from src.models import BookingSchemas, SearchSchema

from src.bookings.router import router as router_bookings
from src.users.router import router as router_users

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
