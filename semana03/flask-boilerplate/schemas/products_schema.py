from pydantic import BaseModel

class CreateProductSchema(BaseModel):
    name: str
    description: str | None = None
    price: float
    stock: int

class UpdateProductSchema(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    stock: int | None = None
    status: bool | None = None