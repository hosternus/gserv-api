from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PostedUser(BaseModel):
    id: int
    name: Optional[str]
    surname: Optional[str]
    address: Optional[str]
    phone: Optional[int]

class CreatedUser(BaseModel):
    phone: int
    code: Optional[int]

class PostOrder(BaseModel):
    userid: int
    uslugaid: int
    runtime: datetime


class SendOrder(BaseModel):
    id: int
    sname: str
    ename: str
    isCompleted: bool
    accepted: bool
    price: float
    serviceid: int


class Feed(BaseModel):
    id: Optional[int]
    mark: int
    feed: str
    name: Optional[str]
    userid: Optional[int]
    serviceid: Optional[int]