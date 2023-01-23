from pydantic import BaseModel
from typing import Optional


class ProductIn(BaseModel):
    title: str
    description: str
    price: float


class ProductOut(ProductIn):
    id: int


class ProductUpdate(ProductIn):
    name: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None