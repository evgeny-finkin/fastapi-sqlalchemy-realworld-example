from fastapi import APIRouter, Depends, HTTPException, Path
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import User, NewUser, AuthenticationUser
from services import postgres, api

router = APIRouter()


@router.post('/login', response_model=User)
async def login(
    session: AsyncSession = Depends(postgres.get_async_session),
    authentication_user: AuthenticationUser = None
):
    is_authenticated = api.users.authentication(session, authentication_user)
    if is_authenticated is False:
        raise HTTPException(status_code=404, detail='User not found')
    user = await api.users.get_user(session, user.email)
    return user


@router.post('/', response_model=User, status_code=201)
async def registration(
    session: AsyncSession = Depends(postgres.get_async_session),
    new_user: NewUser = None
):
    user = await api.users.create_user(session, new_user)
    return user


# @router.get('/', response_model=List[User])
# async def get_users(session: Session = Depends(postgres.get_session), skip: int = 0, limit: int = 10):
#     users = user.get_users(session, skip, limit)
#     return users


# @router.post('/', response_model=User, status_code=201)
# async def add_user(session: Session = Depends(postgres.get_session), userCreate: UserCreate = None):
#     _user = user.create_user(session, userCreate)
#     return _user


# @router.get('/{id}', response_model=User)
# async def get_user(
#     session: AsyncSession = Depends(postgres.get_async_session),
#     id: int = Path(..., description='The id of the user you want to retrive')
# ):
#     _user = await users.get_user(session, id)
#     if _user is None:
#         raise HTTPException(status_code=404, detail='User not found')
#     return _user
