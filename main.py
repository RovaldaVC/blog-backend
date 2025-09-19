from fastapi import FastAPI
from . import models
from database import engine
from routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

    
#If you’re opening an image asynchronously with await, your program will pause just that task until the image is fully loaded—but the event loop (the background “manager” of async tasks) can keep running other things like downloads, API calls, or UI updates.


#tags=["part_name"] will help us find our methods easier in swagger ui.


