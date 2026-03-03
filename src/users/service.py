from src.service.base import BaseService
from src.users.models import Users


class UsersService(BaseService):
    model = Users
