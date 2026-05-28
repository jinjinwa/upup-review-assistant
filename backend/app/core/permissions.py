from fastapi import Depends

from app.core.auth import get_current_user
from app.core.exceptions import ForbiddenException
from app.models import User


def require_admin(user: User = Depends(get_current_user)) -> User:
    if user.role != "admin":
        raise ForbiddenException("Admin role required")
    return user
