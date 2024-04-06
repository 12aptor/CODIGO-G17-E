from pydantic import ValidationError
from models.products_model import ProductModel
from schemas.products_schema import (
    CreateProductSchema,
    UpdateProductSchema
)
from db import db

class ProductController:
    def __init__(self):
        self.model = ProductModel

    def getAll(self):
        try:
            products = self.model.query.filter_by(status=True).all()
            response = [product.toJson() for product in products]
            return response, 200

        except Exception as e:
            return {
                'errors': str(e)
            }, 500

    def create(self, json):
        try:
            validatedData = CreateProductSchema(**json)

            newProduct = self.model(**validatedData.model_dump())

            db.session.add(newProduct)
            db.session.commit()
            return newProduct.toJson(), 201
        
        except ValidationError as e:
            return {
                'errors': e.errors()
            }, 400
        except Exception as e:
            db.session.rollback()
            return {
                'errors': str(e)
            }, 500
        
    def update(self, id: int, json):
        try:
            product = self.model.query.get(id)
            if product is None:
                raise Exception('Product not found')

            validatedData = UpdateProductSchema(**json)
            product.update(validatedData)

            db.session.commit()
            return product.toJson(), 200
        
        except ValidationError as e:
            return {
                'errors': e.errors()
            }, 400
        except Exception as e:
            db.session.rollback()
            return {
                'errors': str(e)
            }, 500
        
    def delete(self, id: int):
        try:
            product = self.model.query.get(id)
            if product is None:
                raise Exception('Product not found')
            
            product.status = False
            
            db.session.commit()
            return {
                'message': 'Product deleted'
            }, 200
        
        except Exception as e:
            return {
                'errors': str(e)
            }, 500
        
    def getById(self, id: int):
        try:
            product = self.model.query.get(id)
            if product is None:
                raise Exception('Product not found')
            
            return product.toJson(), 200
        
        except Exception as e:
            return {
                'errors': str(e)
            }, 500