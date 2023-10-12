import uuid
from typing import Any, Union
from typing_extensions import Annotated

from fastapi import APIRouter, status, Query, HTTPException
from fastapi_pagination.cursor import CursorPage as BaseCursorPage
from fastapi_pagination.ext.cassandra import paginate

from schemas.schemaModels import ClientBase
from db.dataModels import Client_By_Nickmail

CursorPage = BaseCursorPage.with_custom_options(str_cursor=False)

router = APIRouter()


@router.get("/find-all/cursor", status_code=status.HTTP_200_OK, response_model=CursorPage[ClientBase])
def get_clients() -> Any:
    return paginate(Client_By_Nickmail)


@router.get("/find-data/", status_code=status.HTTP_200_OK, response_model=ClientBase)
def get_client_id(nick: Annotated[Union[str, None], Query()], pic_email: Annotated[Union[str, None], Query()] = None):
    res_client = Client_By_Nickmail.objects.filter(
        nick=nick)

    if pic_email is not None:
        res_client = res_client.filter(pic_email=pic_email)

    res_client = res_client.first()

    if res_client is None:
        raise HTTPException(status_code=404, detail="Client not found!")
    else:
        return res_client
