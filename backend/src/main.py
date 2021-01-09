# import type hintes
from typing import Dict


# import dependencies
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles # required to bind a phyisical folder to a virtual path

from database.database import engine
from database.base import Base
from router import images
from router import tags

# create migrations
Base.metadata.create_all(bind=engine)

# initialize application
app = FastAPI()

# bind images folder to images path
app.mount(path="/images", app=StaticFiles(directory="images"), name="static")

# register routers
app.include_router(router = images.router, prefix = "/images")
app.include_router(router = tags.router, prefix="/tags")