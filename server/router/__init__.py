from fastapi import APIRouter
from router import users

router = APIRouter()
router.include_router(users.router, prefix='/users')