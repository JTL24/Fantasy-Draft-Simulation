from fastapi import APIRouter

from . import player


router = APIRouter()

@router.get("/")
async def root():
    return {"message": "API v1"}

router.include_router(player.router, prefix="/player")
