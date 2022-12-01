from fastapi import APIRouter
from router import users, user, profiles, aricles, tags

router = APIRouter()
router.include_router(tags.router, prefix='/api/tags')
router.include_router(aricles.router, prefix='/api/articles')
router.include_router(profiles.router, prefix='/api/profiles')
router.include_router(users.router, prefix='/api/users')
router.include_router(user.router, prefix='/api/user')
