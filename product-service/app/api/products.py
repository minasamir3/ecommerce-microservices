from fastapi import HTTPException, FastAPI, Header, APIRouter
from typing import List
from app.api.models import ProductIn, ProductOut
from app.api import db_manager

products = APIRouter()


@products.get('/', response_model=List[ProductOut])
async def index():
    return await db_manager.get_all_products()


@products.post('/', status_code=201)
async def add_product(payload: ProductIn):
    product_id = await db_manager.add_product(payload)
    response = {
        'id': product_id,
        **payload.dict()
    }
    return response


@products.put('/{id}')
async def update_product(id: int, payload: ProductIn):
    product = await db_manager.get_product(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    update_data = payload.dict(exclude_unset=True)
    product_in_db = ProductIn(**product)

    updated_product = product_in_db.copy(update=update_data)

    return await db_manager.update_product(id, updated_product)


@products.delete('/{id}')
async def delete_product(id: int):
    product = await db_manager.get_product(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return await db_manager.delete_product(id)
