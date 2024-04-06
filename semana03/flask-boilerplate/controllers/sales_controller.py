from models.sales_model import (
    SaleModel,
    SaleDetailModel
)
from schemas.sales_schema import CreateSaleSchema
from pydantic import ValidationError

class SaleController:
    def __init__(self) -> None:
        self.sale_model = SaleModel
        self.sale_detail_model = SaleDetailModel

    def create(self, json):
        try:
            sale = CreateSaleSchema(**json)
            print(sale.model_dump())

            return{
                'ok': True
            }, 201
        except ValidationError as e:
            return {
                'errors': e.errors(),
            }, 400
        except Exception as e:
            return {
                'errors': str(e),
            }, 500