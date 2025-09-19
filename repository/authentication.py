from .. import schemas, models, hashing, Token
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import timedelta

def login(request:schemas.Login, db:Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not hashing.Hash.verify(request.password, user.Password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    
    access_token = Token.create_access_token(data={"sub":user.email})
    return {"access_token":access_token, "token_type":"bearer"}