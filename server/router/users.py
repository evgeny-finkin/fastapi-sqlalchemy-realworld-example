from fastapi import APIRouter, Depends, HTTPException, Path
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import User, NewUser, AuthenticationUser, UserResponse, RequestUser, UpdatedUser
from services import postgres, api

router = APIRouter()


@router.post('/login', response_model=User)
async def authentication(
    session: AsyncSession = Depends(postgres.get_async_session),
    authentication_user: AuthenticationUser = None
):
    # is_authenticated = api.users.authentication(session, authentication_user)
    # if is_authenticated is False:
    #     raise HTTPException(status_code=404, detail='User not found')
    user = await api.users.get_user(session, user.email)
    return user


@router.post('/', response_model=UserResponse, status_code=201)
async def registration(
    session: AsyncSession = Depends(postgres.get_async_session),
    new_user: NewUser = None
):
    await api.users.create_user(session, new_user)
    user_response = UserResponse(
        username=new_user.username,
        email=new_user.email,
        bio=new_user.bio,
        image=new_user.image
    )
    return user_response


@router.get('/', response_model=UserResponse)
async def get_users(
    session: AsyncSession = Depends(postgres.get_async_session),
    request_user: RequestUser = None
):
    # TODO: need to return user from jwt
    user = await api.users.get_user(session, request_user.email)
    user_response = UserResponse(
        username=user.username,
        email=user.email,
        bio=user.bio,
        image=user.image
    )
    return user_response


@router.put('/', status_code=204)
async def update_user(
    session: AsyncSession = Depends(postgres.get_async_session),
    updated_user: UpdatedUser = None
):
    await api.users.update_user(session, updated_user)
