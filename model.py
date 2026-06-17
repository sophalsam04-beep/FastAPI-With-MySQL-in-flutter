# Model in python Programing

from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))
    
