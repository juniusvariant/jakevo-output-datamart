import uuid
from typing import Any, Union
from typing_extensions import Annotated
from datetime import datetime

from fastapi import APIRouter, status, Query, HTTPException
from fastapi_pagination.cursor import CursorPage as BaseCursorPage
from fastapi_pagination.ext.cassandra import paginate

from schemas.schemaModels import ReqLogBase, InsertedReqLogs
from db.dataModels import Request_Logs


CursorPage = BaseCursorPage.with_custom_options(str_cursor=False)


router = APIRouter()


@router.post("/create", response_model=InsertedReqLogs)
def create_requestlog(req_in: ReqLogBase) -> Request_Logs:
    dt_now = datetime.utcnow()
    # loc_wib = dt_now.astimezone(timezone('Asia/jakarta'))

    req = Request_Logs(log_id=uuid.uuid4(), request_body=req_in.request_body,
                       request_date=dt_now, request_by=req_in.request_by)
    req.save()
    return req
