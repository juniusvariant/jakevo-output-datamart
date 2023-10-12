import uuid
from typing import Any, Union
from typing_extensions import Annotated

from fastapi import APIRouter, status, Query, HTTPException
from fastapi_pagination.cursor import CursorPage as BaseCursorPage
from fastapi_pagination.ext.cassandra import paginate

from schemas.schemaModels import OutputDataBase
from db.dataModels import Output_By_Decreeidentity

CursorPage = BaseCursorPage.with_custom_options(str_cursor=False)

router = APIRouter()


@router.get("/find-all/cursor", status_code=status.HTTP_200_OK, response_model=CursorPage[OutputDataBase])
def get_outputs() -> Any:
    return paginate(Output_By_Decreeidentity)


@router.get("/find-data/", status_code=status.HTTP_200_OK, response_model=OutputDataBase)
def get_output_decree(decree_number: Annotated[Union[str, None], Query()], owner_identity_number: Annotated[Union[str, None], Query()] = None):
    res_output = Output_By_Decreeidentity.objects.filter(
        decree_number=decree_number)

    if owner_identity_number is not None:
        res_output = res_output.filter(
            owner_identity_number=owner_identity_number)

    res_output = res_output.first()

    if res_output is None:
        raise HTTPException(status_code=404, detail="Output not found!")
    else:
        return res_output
