from sqlalchemy import Column, Integer, String, Boolean
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    document_type = Column(String(100))
    document_number = Column(String(20), unique=True)
    email = Column(String(200), unique=True)
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
    
    def update(self, data):
        if data.name is not None:
            self.name = data.name
        if data.document_type is not None:
            self.document_type = data.document_type
        if data.document_number is not None:
            self.document_number = data.document_number
        if data.email is not None:
            self.email = data.email
        if data.password is not None:
            self.password = data.password
        if data.status is not None:
            self.status = data.status