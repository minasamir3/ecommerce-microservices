import os
from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY, Float)

from databases import Database

DATABASE_URL = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URL)
metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('phone', String(250)),
    Column('email', String(100))
)

database = Database(DATABASE_URL)
