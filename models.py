from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey=("users.id"))
    
    creator = relationship("User", back_populates="blogs")
#whatever class that has Base is a database material.

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    Password = Column(String)
    
    blogs = relationship("Blog", back_populates="creator")
    
#relationship lets us use another classes data after connection. 
#foreignkey will use the other classes data.