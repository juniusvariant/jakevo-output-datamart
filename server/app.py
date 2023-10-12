import uuid
from contextlib import asynccontextmanager
from typing import Any, Union
from typing_extensions import Annotated
from datetime import datetime
from pytz import timezone

import uvicorn
from cassandra.cluster import Cluster
from cassandra.cqlengine import columns, connection, management, models
from faker import Faker
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel

from fastapi_pagination import add_pagination
from fastapi_pagination.cursor import CursorPage as BaseCursorPage
from fastapi_pagination.ext.cassandra import paginate

faker = Faker()

CursorPage = BaseCursorPage.with_custom_options(str_cursor=False)


class User(models.Model):
    __keyspace__ = "ks"

    identity_number = columns.Text(primary_key=True, index=True)
    name = columns.Text()
    email = columns.Text(primary_key=True, index=True)
    registered_at = columns.DateTime()
    id = columns.UUID(partition_key=True)


class User_By_Identitynumber(models.Model):
    __keyspace__ = "ks"

    identity_number = columns.Text(primary_key=True, index=True)
    name = columns.Text()
    email = columns.Text(primary_key=True, index=True)
    registered_at = columns.DateTime()
    id = columns.UUID()


class UserIn(BaseModel):
    identity_number: str
    name: str
    email: str
    registered_at: datetime


class UserOut(UserIn):
    id: uuid.UUID

    class Config:
        from_attributes = True


@asynccontextmanager
async def lifespan(_: Any) -> None:
    ddl = "CREATE KEYSPACE IF NOT EXISTS ks WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}"
    session.execute(ddl)
    connection.register_connection("cluster1", session=session, default=True)
    management.sync_table(model=User, keyspaces=("ks",))

    dt_now = datetime.utcnow()
    # loc_wib = dt_now.astimezone(timezone('Asia/jakarta'))

    users = [User(id=uuid.uuid4(), identity_number=faker.credit_card_number(), name=faker.name(), email=faker.email(), registered_at=dt_now)
             for _ in range(100)]
    for user in users:
        user.save()
    yield


app = FastAPI(lifespan=lifespan)
session = Cluster(
    [
        "localhost",
    ]
).connect()


@app.post("/users", response_model=UserOut)
def create_user(user_in: UserIn) -> User:
    dt_now = datetime.utcnow()
    # loc_wib = dt_now.astimezone(timezone('Asia/jakarta'))

    user = User(id=uuid.uuid4(), identity_number=user_in.identity_number, name=user_in.name,
                email=user_in.email, registered_at=dt_now)
    user.save()
    return user


@app.get("/users/cursor", response_model=CursorPage[UserOut])
def get_users() -> Any:
    return paginate(User)


# @app.get("/find/{identity_number}/email/{email}", response_model=UserOut)
# def get_users_id(identity_number, email):
#     # q = User.objects(User.identity_number ==
#     #                  identity_number, User.email == email)
#     q = User_By_Identitynumber.objects.filter(identity_number=identity_number)
#     q = q.filter(email=email)
#     res_user = q.get()
#     # res_user = User.objects.get(identity_number=identity_number, email=email)
#     return res_user

@app.get("/find-user/", response_model=UserOut)
def get_users_id(identity_number: Annotated[Union[str, None], Query()], email: Annotated[Union[str, None], Query()] = None):
    # q = User.objects(User.identity_number ==
    #                  identity_number, User.email == email)
    q = User_By_Identitynumber.objects.filter(identity_number=identity_number)

    if email is not None:
        q = q.filter(email=email)

    q = q.first()

    # res_user = q

    if q is None:
        raise HTTPException(status_code=404, detail="User not found!")
    else:
        return q

    # res_user = User.objects.get(identity_number=identity_number, email=email)


add_pagination(app)

# if __name__ == "__main__":
#     uvicorn.run("pagination_scylla:app")
