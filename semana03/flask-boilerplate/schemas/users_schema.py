from pydantic import BaseModel

class CrearUserSchema(BaseModel):
    name: str
    document_type: str
    document_number: str
    email: str
    password: str
    status: bool

class UpdateUserSchema(BaseModel):
    name: str | None = None
    document_type: str | None = None
    document_number: str | None = None
    email: str | None = None
    password: str | None = None
    status: bool | None = None