from pydantic import BaseModel, Field
from typing import Optional

class Player(BaseModel):
    id: int | None = None
    name: Optional[str] = None
    team: str | None = None
    rank: int | None = None
    bye: int | None = None
    position: str | None = None
