from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from db import db

class SaleModel(db.Model):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    total = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    details = relationship('SaleDetailModel')
    user = relationship('UserModel')

    def toJson(self):
        return {
            'id': self.id,
            'total': self.total,
            'user_id': self.user_id,
            'details': [detail.toJson() for detail in self.details],
            'user': self.user.toJson()
        }
    

class SaleDetailModel(db.Model):
    __tablename__ = 'sale_details'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'))
    sale_id = Column(Integer, ForeignKey('sales.id'))

    def toJson(self):
        return {
            'id': self.id,
            'quantity': self.quantity,
            'price': self.price,
            'subtotal': self.subtotal,
            'product_id': self.product_id,
            'sale_id': self.sale_id
        }
