from datetime import date

from fastapi import APIRouter, Depends

from exceptions import RoomCanNotBeBooked
from src.booking.schemas import SBooking
from src.booking.service import BookingService
from src.users.dependencies import get_current_user
from src.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)


@router.get("")
async def get_bookings(
    user: Users = Depends(get_current_user)
) -> list[SBooking]:
    return await BookingService.find_all(
        user_id=user.id
    )


@router.post("")
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user)
):
    booking = await BookingService.add(
        user_id=user.id,
        room_id=room_id,
        date_from=date_from,
        date_to=date_to
    )
    if not booking:
        raise RoomCanNotBeBooked()
