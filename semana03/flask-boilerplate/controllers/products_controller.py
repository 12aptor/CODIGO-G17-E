from pydantic import ValidationError
from models.products_model import ProductModel
from schemas.products_schema import CreateProductSchema
from db import db

class ProductController:
    def __init__(self):
        self.model = ProductModel

    def getAll(self):
        pass

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