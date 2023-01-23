from fastapi import FastAPI
from app.api.users import users
from app.api.db import metadata, database, engine

metadata.create_all(engine)
app = FastAPI()
app.include_router(users, prefix='/api/v1/users', tags=['users'])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()