from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    func
)
from db import db

class ProductModel(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200), nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    status = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


    def toJson(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    def update(self, data):
        if data.name is not None:
            self.name = data.name
        if data.description is not None:
            self.description = data.description
        if data.price is not None:
            self.price = data.price
        if data.stock is not None:
            self.stock = data.stock
        if data.status is not None:
            self.status = data.status