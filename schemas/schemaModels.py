from pydantic import BaseModel
from uuid import UUID
from datetime import date, datetime


class OwnerIn(BaseModel):
    identity_number: str
    name: str
    email: str
    phone: str
    address: str
    village: str
    district: str
    city: str
    province: str
    owner_type: str

    class Config:
        from_attributes = True


class OwnerBase(BaseModel):
    owner_id: UUID
    identity_number: str
    name: str
    email: str
    phone: str
    address: str
    village: str
    district: str
    city: str
    province: str
    owner_type: str

    class Config:
        from_attributes = True


class ApplicantBase(BaseModel):
    applicant_id: UUID
    identity_number: str
    name: str
    email: str
    phone: str
    address: str
    village: str
    district: str
    city: str
    province: str

    class Config:
        from_attributes = True


class PermitBase(BaseModel):
    permit_id: UUID
    jakevo_permit_code: str
    oss_permit_id: str
    oss_permit_name: str
    name: str
    sector: str

    class Config:
        from_attributes = True


class OutputDataBase(BaseModel):
    output_id: UUID
    decree_number: str
    owner_identity_number: str
    owner_name: str
    applicant_identity_number: str
    applicant_name: str
    application_date: date
    issued_date: date
    expired_date: date
    permit_type: str
    application_type: str
    permit_id: str
    permit_name: str
    permit_sector: str
    authority: str
    jurisdiction: str
    data_source: str

    class Config:
        from_attributes = True


class OutputFileBase(BaseModel):
    file_id: UUID
    decree_number: str
    identity_number: str
    issued_date: date
    expired_date: date
    file_location: str
    data_source: str

    class Config:
        from_attributes = True


class ReqLogBase(BaseModel):
    log_id: UUID
    request_body: str
    request_by: str

    class Config:
        from_attributes = True


class ClientBase(BaseModel):
    client_id: UUID
    name: str
    nick: str
    pic_name: str
    pic_email: str
    pic_phone: str

    class Config:
        from_attributes = True


class InsertedReqLogs(ReqLogBase):
    request_date: datetime
    information: str = 'Insert Data Request Log Success.'

    class Config:
        from_attributes = True


class UserIn(BaseModel):
    name: str
    email: str


class UserOut(UserIn):
    id: UUID
    registered_at: datetime

    class Config:
        from_attributes = True
