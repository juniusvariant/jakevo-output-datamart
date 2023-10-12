import uuid
from typing import Any, Union
from typing_extensions import Annotated

from fastapi import APIRouter, status, Query, HTTPException
from fastapi_pagination.cursor import CursorPage as BaseCursorPage
from fastapi_pagination.ext.cassandra import paginate

from schemas.schemaModels import ApplicantBase
from db.dataModels import Applicant_By_Identitynumber

CursorPage = BaseCursorPage.with_custom_options(str_cursor=False)

router = APIRouter()


@router.get("/find-all/cursor", status_code=status.HTTP_200_OK, response_model=CursorPage[ApplicantBase])
def get_applicants() -> Any:
    return paginate(Applicant_By_Identitynumber)


@router.get("/find-data/", status_code=status.HTTP_200_OK, response_model=ApplicantBase)
def get_applicant_id(identity_number: Annotated[Union[str, None], Query()], email: Annotated[Union[str, None], Query()] = None):
    res_applicant = Applicant_By_Identitynumber.objects.filter(
        identity_number=identity_number)

    if email is not None:
        res_applicant = res_applicant.filter(email=email)

    res_applicant = res_applicant.first()

    if res_applicant is None:
        raise HTTPException(status_code=404, detail="Applicant not found!")
    else:
        return res_applicant
