from typing import Callable, List

from fastapi import Body, FastAPI, HTTPException, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute

from . import v1


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Fantasy Football API"}

app.include_router(v1.router, prefix="/v1")
app.include_router(v1.router, prefix="/latest")
