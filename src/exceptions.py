from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Server error"

    def __init__(self, detail: str | None = None):
        super().__init__(
            status_code=self.status_code,
            detail=self.detail,
        )


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User Already Exists"


class IncorrectEmailOrPasswordException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect Email Or Password"


class TokenExpiredException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token Has Expired"


class TokenAbsentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token Absent"


class RoomCanNotBeBooked(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "No Rooms Left"


class IncorrectTokenFormatException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect Token Format"


class UserIsNotPresentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "User is not present"


class CannotBookHotelForLongPeriod(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Can not book hotel for long period"


class DateFromCannotBeAfterDateTo(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Date from can not be after date to"
