from fastapi import APIRouter, Depends, HTTPException, Path
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import User, UserCreate
from services import user, postgres

router = APIRouter()


# @router.get('/', response_model=List[User])
# async def get_users(session: Session = Depends(postgres.get_session), skip: int = 0, limit: int = 10):
#     users = user.get_users(session, skip, limit)
#     return users


# @router.post('/', response_model=User, status_code=201)
# async def add_user(session: Session = Depends(postgres.get_session), userCreate: UserCreate = None):
#     _user = user.create_user(session, userCreate)
#     return _user


@router.get('/{id}', response_model=User)
async def get_user(
    session: AsyncSession = Depends(postgres.get_async_session),
    id: int = Path(..., description='The id of the user you want to retrive')
):
    _user = await user.get_user(session, id)
    if _user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return _user
