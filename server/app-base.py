from fastapi import FastAPI
from fastapi_pagination import add_pagination

from configs import app_config
from routers import user_router, owner_router, applicant_router, permit_router, output_router, outputfile_router, client_router, requestlog_router

from configs.db_config import lifespan

conf = app_config.Settings()

app_title = conf.TITLE
app_desc = conf.DESCRIPTION
app_ver = conf.VERSION
tags_metadata = conf.METADATA
docs = conf.DOCS_URL
redoc = conf.REDOC_URL


app = FastAPI(
    lifespan=lifespan,
    title=app_title,
    description=app_desc,
    version=app_ver,
    openapi_tags=tags_metadata,
    docs_url=docs,
    redoc_url=redoc,
    swagger_ui_parameters={"docExpansion": "none"},
)


app.include_router(user_router.router, tags=['User End-Point'], prefix='/user')
app.include_router(owner_router.router, tags=[
                   'Owner End-Point'], prefix='/owner')
app.include_router(applicant_router.router, tags=[
                   'Applicant End-Point'], prefix='/applicant')
app.include_router(permit_router.router, tags=[
                   'Permit End-Point'], prefix='/permit')
app.include_router(output_router.router, tags=[
                   'Output End-Point'], prefix='/output')
app.include_router(outputfile_router.router, tags=[
                   'Output File End-Point'], prefix='/outputfile')
app.include_router(client_router.router, tags=[
                   'Client End-Point'], prefix='/client')
app.include_router(requestlog_router.router, tags=[
                   'Request Log End-Point'], prefix='/requestlog')


@app.get("/")
async def root():
    return {"message": "Welcome to Jakevo Permit Output Datamart API"}

add_pagination(app)
