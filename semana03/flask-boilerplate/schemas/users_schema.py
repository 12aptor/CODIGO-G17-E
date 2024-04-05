from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    document_type: str
    document_number: str
    email: str
    password: str
    status: bool
