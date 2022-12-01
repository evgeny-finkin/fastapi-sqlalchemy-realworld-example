from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from services import postgres, api, jwt
from schemas import User, UpdatedUser
router = APIRouter()


@router.get('/', response_model=User)
async def get_current_user(
    session: AsyncSession = Depends(postgres.get_async_session),
    token: str = None
):
    obj = await jwt.decode(token)
    user = await api.users.get_user(session, obj.email)
    return user


@router.put('/', response_model=User)
async def get_current_user(
    session: AsyncSession = Depends(postgres.get_async_session),
    token: str = None,
    updated_user: UpdatedUser = None
):
    is_token_valid = await jwt.validate(token)
    if is_token_valid == False:
        raise HTTPException(status_code=401, detail='Invalid token')
    user = await api.users.update_user(session, updated_user)
    return user
