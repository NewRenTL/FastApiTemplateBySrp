from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.services import userService
from app.models.userModels import UserCreate,UserResponse,UserUpdate,UserList
from app.core.database import get_db;


router = APIRouter();

#Query
@router.get("/get/{id}",response_model=UserResponse)
async def getById(id:int,db:AsyncSession = Depends(get_db)):
    obtained_user = await userService.getById(id,db)
    if not obtained_user:
        print("entro")
        raise HTTPException(status_code=404,detail="User hasn't been found")
    return obtained_user

#Query
@router.get("/list",response_model=list[UserList])
async def list_users(db:AsyncSession = Depends(get_db)):
    obtained_users = await userService.listAll(db);
    if not obtained_users:
          raise HTTPException(status_code=405,detail="Users haven't been found")
    return obtained_users

#Command
@router.post("/",response_model=UserResponse)
async def create_user(user:UserCreate,db:AsyncSession = Depends(get_db)):
    new_user = await userService.create_user(user.name,user.email,db)
    return new_user

#Command
@router.put("/update",response_model=UserResponse)
async def update_user(user:UserUpdate,db:AsyncSession = Depends(get_db)):
    update_user = await userService.update_user(user.id,user.name,user.email,db);

    if not update_user:
        raise HTTPException(status_code=404,detail="User hasn't been found to create")
    return update_user

@router.delete("/delete/{id}",response_model=UserResponse)
async def delete_user(id:int,db:AsyncSession = Depends(get_db)):
    delete_user = await userService.deleteUser(id,db);

    if not delete_user:
        raise HTTPException(status_code=404,detail="User hasn't been found to delete")
    return delete_user
