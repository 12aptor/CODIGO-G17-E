from pydantic import BaseModel


class SaleDetailSchema(BaseModel):
    quantity: int
    price: float
    subtotal: float
    product_id: int

class CreateSaleSchema(BaseModel):
    total: float
    user_id: int
    details: list[SaleDetailSchema]