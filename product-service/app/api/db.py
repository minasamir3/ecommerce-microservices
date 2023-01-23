import os
from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY, Float)

from databases import Database

DATABASE_URL = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URL)
metadata = MetaData()

products = Table(
    'products',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(50)),
    Column('description', String(250)),
    Column('price', Float)
)

database = Database(DATABASE_URL)
