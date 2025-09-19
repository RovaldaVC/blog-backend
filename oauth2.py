from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
import Token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#tokenUrl means which @ url you will use the auth for.

def get_current_user(token:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return Token.verify_token(token, credentials_exception)