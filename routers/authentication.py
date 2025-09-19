from fastapi import APIRouter, Depends
from .. import database
from sqlalchemy.orm import Session
from ..repository import authentication
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)

@router.post("/")
def login(request:OAuth2PasswordRequestForm, db:Session=Depends[database.get_db]):
    return authentication.login(request, db)