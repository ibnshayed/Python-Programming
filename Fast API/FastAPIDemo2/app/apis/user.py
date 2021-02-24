from fastapi import APIRouter, File, UploadFile, Form, HTTPException, Depends
from typing import Optional


router = APIRouter(
    prefix="/user",
    tags=["User"]
)

items = {"foo": "The Foo Wrestlers"}

async def page_params(page: Optional[int] = 0, size: Optional[int] = 10):
    return {'page': page, 'size': size}

@router.get("/")
async def index():
    return "This is from user module"

@router.post("/")
async def index(file: UploadFile = File(...), token: str = Form(...),):
    return {'File': file, 'Token': token}

@router.get("/items/{item_id}")
async def read_item(item_id: str, pagination: dict = Depends(page_params)):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}