from fastapi import FastAPI
from app.api.products import products
from app.api.db import metadata, database, engine

metadata.create_all(engine)
app = FastAPI()
app.include_router(products, prefix='/api/v1/products', tags=['products'])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()