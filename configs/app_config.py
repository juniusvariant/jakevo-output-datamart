from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    TITLE: str = "#Jakevo Output Data Mart"
    DESCRIPTION: str = "Jakevo Output Data Mart APIs Documentation"
    VERSION: str = "1.0.0"
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redocs"
    METADATA: list = [
        {
            "name": "User End-Point",
            "description": "Operations with all about **User**.",
        }, {
            "name": "Owner End-Point",
            "description": "Operations with all about **Owner**.",
        },
        {
            "name": "Permit End-Point",
            "description": "Operations with all about **Permit**.",
        },
        {
            "name": "Output End-Point",
            "description": "Operations with all about **Output**.",
        }, {
            "name": "Output File End-Point",
            "description": "Operations with all about **Output File**.",
        },
        {
            "name": "Client End-Point",
            "description": "Operations with all about **Client**.",
        },
        {
            "name": "Request Log End-Point",
            "description": "Operations with all about **Request Log**.",
        }

    ]
