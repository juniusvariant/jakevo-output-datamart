import uuid
from typing import Any, Union
from typing_extensions import Annotated

from fastapi import APIRouter, status, Query, HTTPException
from fastapi_pagination.cursor import CursorPage as BaseCursorPage
from fastapi_pagination.ext.cassandra import paginate

from schemas.schemaModels import OutputFileBase
from db.dataModels import Output_File_By_Decreeidentity

CursorPage = BaseCursorPage.with_custom_options(str_cursor=False)

router = APIRouter()


@router.get("/find-all/cursor", status_code=status.HTTP_200_OK, response_model=CursorPage[OutputFileBase])
def get_outputs() -> Any:
    return paginate(Output_File_By_Decreeidentity)


@router.get("/find-data/", status_code=status.HTTP_200_OK, response_model=OutputFileBase)
def get_outputfile_decree(decree_number: Annotated[Union[str, None], Query()], owner_identity_number: Annotated[Union[str, None], Query()] = None):
    res_outputfile = Output_File_By_Decreeidentity.objects.filter(
        decree_number=decree_number)

    if owner_identity_number is not None:
        res_outputfile = res_outputfile.filter(
            owner_identity_number=owner_identity_number)

    res_outputfile = res_outputfile.first()

    if res_outputfile is None:
        raise HTTPException(status_code=404, detail="Output File not found!")
    else:
        return res_outputfile
