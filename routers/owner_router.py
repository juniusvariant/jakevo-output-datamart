import uuid
from typing import Any, Union
from typing_extensions import Annotated

from fastapi import APIRouter, status, Query, HTTPException
from fastapi_pagination.cursor import CursorPage as BaseCursorPage
from fastapi_pagination.ext.cassandra import paginate

from schemas.schemaModels import OwnerBase
from db.dataModels import Owner_By_Identitynumber

CursorPage = BaseCursorPage.with_custom_options(str_cursor=False)

router = APIRouter()


@router.get("/find-all/cursor", status_code=status.HTTP_200_OK, response_model=CursorPage[OwnerBase])
def get_owners() -> Any:
    return paginate(Owner_By_Identitynumber)


@router.get("/find-data/", status_code=status.HTTP_200_OK, response_model=OwnerBase)
def get_owner_id(identity_number: Annotated[Union[str, None], Query()], email: Annotated[Union[str, None], Query()] = None):
    res_owner = Owner_By_Identitynumber.objects.filter(
        identity_number=identity_number)

    if email is not None:
        res_owner = res_owner.filter(email=email)

    res_owner = res_owner.first()

    if res_owner is None:
        raise HTTPException(status_code=404, detail="Owner not found!")
    else:
        return res_owner
