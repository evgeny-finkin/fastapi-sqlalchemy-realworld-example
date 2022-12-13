from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from services import postgres, api, jwt
from schemas import User, UpdatedUser, RequestUser
router = APIRouter()


@router.get('/', response_model=User)
async def get_current_user(
    session: AsyncSession = Depends(postgres.get_async_session),
    # token: str = None,
    request_user: RequestUser = None
):
    # obj = await jwt.decode(token)
    user = await api.users.get_user(session, request_user.email)
    return user


@router.put('/', status_code=204)
async def update_user(
    session: AsyncSession = Depends(postgres.get_async_session),
    updated_user: UpdatedUser = None
):
    await api.users.update_user(session, updated_user)
