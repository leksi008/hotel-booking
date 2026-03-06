from fastapi import APIRouter, HTTPException, status, Depends
from starlette.responses import Response

from exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException
from src.users.auth import get_password_hash, authenticate_user, create_access_token
from src.users.dependencies import get_current_user
from src.users.models import Users
from src.users.schemas import SUserAuth
from src.users.service import UsersService

router = APIRouter(
    prefix="/auth",
    tags=["auth & users"],
)


@router.post("/register", status_code=201)
async def register_user(user_data: SUserAuth):
    existing_user = await UsersService.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersService.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException()
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie(
        key="booking_access_token",
        value=access_token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=3600
    )
    return {"status": "ok"}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie(
        key="booking_access_token"
    )
    return {"status": "ok"}


@router.get("/me")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user
