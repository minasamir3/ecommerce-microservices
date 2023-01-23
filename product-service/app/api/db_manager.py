from app.api.models import ProductIn, ProductOut, ProductUpdate
from app.api.db import products, database


async def add_product(payload: ProductIn):
    query = products.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_all_products():
    query = products.select()
    return await database.fetch_all(query=query)


async def get_product(id):
    query = products.select(products.c.id==id)
    return await database.fetch_one(query=query)


async def delete_product(id: int):
    query = products.delete().where(products.c.id==id)
    return await database.execute(query=query)


async def update_product(id: int, payload: ProductIn):
    query = (
        products
        .update()
        .where(products.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
