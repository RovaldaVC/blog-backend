from pydantic import BaseModel
from typing import List, Optional

class BlogBase(BaseModel): 
    title:str
    body:str

class Blog(BlogBase):
    class Config():
        orm_mode = True
#schema models which are made for validations of body parameters will be identified af response_model inside the method @
#orm_mode true means while using crud methods which comes from sqlite.orm the responce will be in dict form and type errors will be solved.

class showBlog2(BaseModel):
    title:str
    class Config():
        orm_mode = True
#if i put this in the response_model ot the get method i will only get the title.

class User(BaseModel):
    name:str
    email:str
    password:str

class showUser(BaseModel):
    class Config():
        orm_mode = True
        
    name:str
    email:str
    blogs : List[Blog] = []
    
class showBlog(BaseModel):
    title:str
    body:str
    creator:showUser
    
    class Config():
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
    