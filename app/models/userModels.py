from pydantic import BaseModel
from typing import Optional



class UserCreate(BaseModel):
    name:str
    email:str


class UserResponse(BaseModel):
    name:str
    email:str

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    id:int
    name:Optional[str] = None
    email:Optional[str] = None
    class Config:
        orm_mode = True

class UserList(BaseModel):
    id:int 
    name: str
    email:str
    class Config:
        orm_mode = True