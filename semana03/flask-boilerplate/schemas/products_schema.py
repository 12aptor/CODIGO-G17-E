from pydantic import BaseModel

class CreateProductSchema(BaseModel):
    name: str
    description: str | None = None
    price: float
    stock: int