from sqlalchemy import Column, Integer, Float, ForeignKey
from db import db

class SaleModel(db.Model):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    total = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

class SaleDetailModel(db.Model):
    __tablename__ = 'sale_details'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'))
    sale_id = Column(Integer, ForeignKey('sales.id'))
