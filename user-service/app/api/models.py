from pydantic import BaseModel
from typing import Optional


class UserIn(BaseModel):
    name: str
    phone: str
    email: str


class UserOut(UserIn):
    id: int


class UserUpdate(UserIn):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
