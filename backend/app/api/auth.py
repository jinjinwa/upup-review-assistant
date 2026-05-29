from fastapi import APIRouter, Depends
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.core.auth import create_access_token, get_current_user
from app.core.database import get_db
from app.core.exceptions import ConflictException, UnauthorizedException
from app.core.password import hash_password, verify_password
from app.core.response import success_response
from app.models import User
from app.schemas.auth import LoginRequest, RegisterRequest, TokenOut, UserOut

router = APIRouter(prefix="/api/auth", tags=["auth"])


def _user_out(user: User) -> dict:
    return UserOut(
        id=user.id,
        username=user.username,
        email=user.email,
        role=user.role,
        is_active=user.is_active,
    ).model_dump()


@router.post("/register")
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.scalar(
        select(User).where(or_(User.email == payload.email, User.username == payload.username))
    )
    if existing:
        raise ConflictException("Email or username already exists")

    user = User(
        username=payload.username,
        email=payload.email,
        password_hash=hash_password(payload.password),
        role="user",
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    token = create_access_token(user)
    return success_response(TokenOut(access_token=token, user=_user_out(user)).model_dump())


@router.post("/login")
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.scalar(select(User).where(User.email == payload.email))
    if user is None or not verify_password(payload.password, user.password_hash):
        raise UnauthorizedException("Invalid email or password")
    if not user.is_active:
        raise UnauthorizedException("User is inactive")
    token = create_access_token(user)
    return success_response(TokenOut(access_token=token, user=_user_out(user)).model_dump())


@router.get("/me")
def me(user: User = Depends(get_current_user)):
    return success_response(_user_out(user))
