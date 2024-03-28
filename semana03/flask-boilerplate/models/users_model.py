from sqlalchemy import Column, Integer, String, Boolean
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    document_type = Column(String(100))
    document_number = Column(String(20))
    email = Column(String(200))
    password = Column(String(200))
    status = Column(Boolean)

    def __repr__(self) -> str:
        return '<User %r>' % self.name
    
    def toJson(self):
        return {
            'id': self.id,
            'name': self.name,
            'document_type': self.document_type,
            'document_number': self.document_number,
            'email': self.email,
            'password': self.password,
            'status': self.status
        }