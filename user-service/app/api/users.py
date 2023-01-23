from fastapi import HTTPException, FastAPI, Header, APIRouter
from typing import List
from app.api.models import UserIn, UserOut
from app.api import db_manager

users = APIRouter()


@users.get('/', response_model=List[UserOut])
async def index():
    return await db_manager.get_all_users()


@users.post('/', status_code=201)
async def add_user(payload: UserIn):
    user_id = await db_manager.add_user(payload)
    response = {
        'id': user_id,
        **payload.dict()
    }
    return response


@users.put('/{id}')
async def update_user(id: int, payload: UserIn):
    user = await db_manager.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = payload.dict(exclude_unset=True)
    user_in_db = UserIn(**user)

    updated_user = user_in_db.copy(update=update_data)

    return await db_manager.update_user(id, updated_user)


@users.delete('/{id}')
async def delete_user(id: int):
    user = await db_manager.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await db_manager.delete_user(id)
