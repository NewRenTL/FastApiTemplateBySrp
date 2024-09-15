from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.entities.user import User


async def get_user_by_email(email:str,db:AsyncSession):
    result = await db.execute(select(User).filter(User.email == email));
    user = result.scalar_one_or_none();
    return user


async def create_user(name:str,email:str,db:AsyncSession):
    
    new_user = User(name=name,email = email);
    
    db.add(new_user);

    await db.commit();

    await db.refresh(new_user);

    return new_user

async def update_user(id:int,name:str,email:str,db:AsyncSession):

    result_command = await db.execute(select(User).filter(User.id == id));
    
    obtained_user = result_command.scalar_one_or_none();

    if obtained_user:
        if name:
            obtained_user.name = name
        if email:
            obtained_user.email = email
        await db.commit()
        await db.refresh(obtained_user)
        return obtained_user
    
    return None

async def getById(id:int,db:AsyncSession):

    result_query = await db.execute(select(User).filter(User.id == id));

    obtained_user = result_query.scalar_one_or_none();

    if obtained_user:

        return obtained_user;

    return None
        
async def deleteUser(id:int,db:AsyncSession):

    result_query = await db.execute(select(User).filter(User.id == id));
    obtained_user = result_query.scalar_one_or_none();

    if obtained_user:
        copy_beforeModel = obtained_user;
        await db.delete(obtained_user);
        await db.commit();
        return copy_beforeModel;
    return None
        

async def listAll(db:AsyncSession):

    result_query = await db.execute(select(User))

    users = result_query.scalars().all();

    print(users)

    return users
