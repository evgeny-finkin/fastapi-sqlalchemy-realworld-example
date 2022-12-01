from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession

from services import postgres, api, jwt
from schemas import Profile
router = APIRouter()


@router.get('/{slug}/comments/favorite')
async def get_tags(
    session: AsyncSession = Depends(postgres.get_async_session),
):
    # obj = await jwt.decode(token)
    await api.tags.get_tags(session)
    return None
