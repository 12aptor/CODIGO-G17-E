from models.sales_model import (
    SaleModel,
    SaleDetailModel
)
from models.products_model import ProductModel
from schemas.sales_schema import CreateSaleSchema
from pydantic import ValidationError
from db import db

class SaleController:
    def __init__(self) -> None:
        self.product_model = ProductModel
        self.sale_model = SaleModel
        self.sale_detail_model = SaleDetailModel

    def create(self, json):
        try:
            validatedData = CreateSaleSchema(**json)
            # Comprobar que existan los productos que se quieren vender
            for detail in validatedData.details:
                product = self.product_model.query.get(detail.product_id)
                if product.stock >= detail.quantity:
                    product.stock -= detail.quantity
                else:
                    raise Exception(f'Producto {product.name} sin stock suficiente')
            # Crear la venta
            newSale = self.sale_model(
                user_id=validatedData.user_id,
                total=validatedData.total
            )
            db.session.add(newSale)
            db.session.flush()

            # Crear los detalles de la venta
            newDetails = []
            for detail in validatedData.details:
                newDetail = self.sale_detail_model(
                    quantity=detail.quantity,
                    price=detail.price,
                    subtotal=detail.subtotal,
                    product_id=detail.product_id,
                    sale_id=newSale.id
                )
                newDetails.append(newDetail)
            db.session.add_all(newDetails)
            db.session.commit()

            return newSale.toJson(), 201
        except ValidationError as e:
            return {
                'errors': e.errors(),
            }, 400
        except Exception as e:
            db.session.rollback()
            return {
                'errors': str(e),
            }, 500
        
    def getAll(self):
        try:
            sales = self.sale_model.query.order_by(self.sale_model.id.desc()).all()
            response = [sale.toJson() for sale in sales]
            return response, 200
        except Exception as e:
            return {
                'errors': str(e),
            }, 500