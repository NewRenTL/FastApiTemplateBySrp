from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database import engine
from app.controllers import userControllers


app = FastAPI();

@asynccontextmanager
async def app_lifecycle(app: FastAPI):
   
    yield
    
    await engine.dispose();


app = FastAPI(lifespan=app_lifecycle)

#Controller prefixes
app.include_router(userControllers.router,prefix="/users")
