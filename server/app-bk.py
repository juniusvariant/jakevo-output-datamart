import uuid
from contextlib import asynccontextmanager
from typing import Any

from configs import app_config
from routers import user_router, owner_router, applicant_router

import uvicorn
from cassandra.cluster import Cluster
from cassandra.cqlengine import columns, connection, management, models
from faker import Faker
from fastapi import FastAPI, status
from pydantic import BaseModel

from fastapi_pagination import add_pagination
# from fastapi_pagination.cursor import CursorPage as BaseCursorPage
# from fastapi_pagination.ext.cassandra import paginate

# from db.config import lifespan
from configs.db_config import lifespan

conf = app_config.Settings()

app_title = conf.TITLE
app_desc = conf.DESCRIPTION
app_ver = conf.VERSION
tags_metadata = conf.METADATA

# CursorPage = BaseCursorPage.with_custom_options(str_cursor=False)


# class User(models.Model):
#     __keyspace__ = "ks"

#     id = columns.UUID(primary_key=True)
#     name = columns.Text()
#     email = columns.Text(primary_key=True)


# class UserIn(BaseModel):
#     name: str
#     email: str


# class UserOut(UserIn):
#     id: uuid.UUID

#     class Config:
#         orm_mode = True


app = FastAPI(
    lifespan=lifespan,
    title=app_title,
    description=app_desc,
    version=app_ver,
    openapi_tags=tags_metadata
)
# app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Jakevo Permit Output Datamart API"}

app.include_router(user_router.router, tags=['User End-Point'], prefix='/user')

app.include_router(user_router.router, tags=[
                   'Owner End-Point'], prefix='/owner')

app.include_router(user_router.router, tags=[
                   'Applicant End-Point'], prefix='/applicant')

# @app.post("/users", status_code=status.HTTP_201_CREATED, response_model=UserOut)
# def create_user(user_in: UserIn) -> User:
#     user = User(id=uuid.uuid4(), name=user_in.name, email=user_in.email)
#     user.save()
#     return user


# @app.get("/users/cursor", response_model=CursorPage[UserOut])
# def get_users() -> Any:
#     return paginate(User)


# @app.get("/users/{user_id}", response_model=UserOut)
# def get_users_id(user_id):
#     res_user = User.objects.get(id=user_id)
#     return res_user


add_pagination(app)

# if __name__ == "__main__":
#     uvicorn.run("pagination_scylla:app")
