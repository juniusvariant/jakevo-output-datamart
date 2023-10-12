import uuid
from typing import Any, Union
from typing_extensions import Annotated
from datetime import datetime

from fastapi import APIRouter, status, Query, HTTPException
from fastapi_pagination.cursor import CursorPage as BaseCursorPage
from fastapi_pagination.ext.cassandra import paginate

from schemas.schemaModels import UserIn, UserOut
from db.dataModels import User, User_By_Identitynumber

CursorPage = BaseCursorPage.with_custom_options(str_cursor=False)

router = APIRouter()


@router.post("/insert", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_user(user_in: UserIn) -> User:
    user = User(id=uuid.uuid4(), name=user_in.name,
                email=user_in.email, registered_at=datetime.utcnow())
    user.save()
    return user


@router.get("/find-all/cursor", status_code=status.HTTP_200_OK, response_model=CursorPage[UserOut])
def get_users() -> Any:
    return paginate(User_By_Identitynumber)


@router.get("/find-data/", status_code=status.HTTP_200_OK, response_model=UserOut)
def get_users_id(identity_number: Annotated[Union[str, None], Query()], email: Annotated[Union[str, None], Query()] = None):
    res_user = User_By_Identitynumber.objects.filter(
        identity_number=identity_number)

    if email is not None:
        res_user = res_user.filter(email=email)

    res_user = res_user.first()

    if res_user is None:
        raise HTTPException(status_code=404, detail="User not found!")
    else:
        return res_user
