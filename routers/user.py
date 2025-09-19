from fastapi import APIRouter, Depends, status
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import users
from .. import oauth2
router = APIRouter(
    prefix="/user",
    tags=["Users"]
)
#prefix means no need to insert the url to @ anymore unless somthing continiued.
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.showUser)
def create_user(request:schemas.User, db: Session = Depends(database.get_db)):
    return users.create(request, db)

@router.get("/{id}", response_model=schemas.showUser)
def get_user(id:int, db: Session = Depends(database.get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return users.find(id, db)