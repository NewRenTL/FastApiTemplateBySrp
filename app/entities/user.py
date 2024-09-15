from sqlalchemy import Column,Integer,String
from app.core.database import Base

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema':'schemaflask1'}

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100),nullable=False)
    email = Column(String(100),nullable=False)