import uuid
from typing import Any, Union
from typing_extensions import Annotated

from fastapi import APIRouter, status, Query, HTTPException
from fastapi_pagination.cursor import CursorPage as BaseCursorPage
from fastapi_pagination.ext.cassandra import paginate

from schemas.schemaModels import PermitBase
from db.dataModels import Permit_By_Jakevocode

CursorPage = BaseCursorPage.with_custom_options(str_cursor=False)

router = APIRouter()


@router.get("/find-all/cursor", status_code=status.HTTP_200_OK, response_model=CursorPage[PermitBase])
def get_permits() -> Any:
    return paginate(Permit_By_Jakevocode)


@router.get("/find-data/", status_code=status.HTTP_200_OK, response_model=PermitBase)
def get_permit_id(jakevo_permit_code: Annotated[Union[str, None], Query()], sector: Annotated[Union[str, None], Query()] = None):
    res_permit = Permit_By_Jakevocode.objects.filter(
        jakevo_permit_code=jakevo_permit_code)

    if sector is not None:
        res_permit = res_permit.filter(sector=sector)

    res_permit = res_permit.first()

    if res_permit is None:
        raise HTTPException(status_code=404, detail="Permit not found!")
    else:
        return res_permit
