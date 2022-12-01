from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession

from services import postgres, api, jwt
from schemas import Profile
router = APIRouter()


@router.get('/{username}', response_model=Profile)
async def getProfile(
    session: AsyncSession = Depends(postgres.get_async_session),
    username: str = Path(...,
                         description='The username of the profile you want to retrive'),
    token: str = None
):
    # obj = await jwt.decode(token)
    profile = await api.profiles.get_profile(session, username)
    return profile


@router.post('/{username}/follow', response_model=Profile)
async def follow_user(
    session: AsyncSession = Depends(postgres.get_async_session),
    username: str = Path(...,
                         description='The username of the profile you want to retrive'),
    token: str = None
):
    obj = await jwt.decode(token)
    profile = await api.profiles.follow(session, obj.username)
    return profile


@router.delete('/{username}/follow', response_model=Profile)
async def unfollow_user(
    session: AsyncSession = Depends(postgres.get_async_session),
    username: str = Path(...,
                         description='The username of the profile you want to retrive'),
    token: str = None
):
    obj = await jwt.decode(token)
    profile = await api.profiles.unfollow(session, obj.username)
    return profile
