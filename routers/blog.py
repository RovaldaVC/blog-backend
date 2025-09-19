from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

@router.get("/", response_model=List[schemas.showBlog])
def find(db: Session = Depends(database.get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.create(request, db)

@router.get("/{id}", response_model=schemas.showBlog,status_code=200)
def find_one(id:int, db: Session = Depends(database.get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.get_one(id, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(database.get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.delete(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog,db: Session = Depends(database.get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)