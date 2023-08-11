from fastapi import APIRouter, Response, status
from typing import List
from ... import struct
from ... import service

router = APIRouter()

@router.get("/")
async def get_list() -> List[struct.player.Player]:
    player_list = service.player.get_list()
    return player_list

@router.get("/{id}")
async def get_player(id: int) -> struct.player.Player:
    player = service.player.get(id)
    return player

# @router.post("/", status_code=201)
# async def create_player(player: struct.player.Player) -> struct.player.Player:
#     new_player = service.player.create(player)
#     return new_player

# @router.put("/{id}")
# async def update_player(id: int, player: struct.player.Player) -> struct.player.Player:
#     updated_player = service.player.update(id, player)
#     return updated_player
