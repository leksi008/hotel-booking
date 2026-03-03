from fastapi import APIRouter, Depends

from src.booking.service import BookingService
from src.users.dependencies import get_current_user
from src.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) : #-> list[SBooking]:
    return await BookingService.find_all(user_id=user.id)
