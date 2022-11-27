from fastapi import APIRouter, Path, Query
from typing import List

from schemas import User

router = APIRouter()

users = []


@router.get('/', response_model=List[User])
async def get_users():
    return users


@router.get('/{id}', response_model=User)
async def get_user(
    id: int = Path(..., description='The id of the user you want to retrive')
):
    return users[id]


@router.post('/', response_model=User)
async def add_user(user: User):
    users.append(user)
    return user
