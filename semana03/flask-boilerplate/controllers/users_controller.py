from models.users_model import UserModel
from db import db
from pydantic import ValidationError
from schemas.users_schema import CrearUserSchema, UpdateUserSchema
import bcrypt

class UserController:
    def __init__(self):
        self.model = UserModel

    def getAll(self):
        try:
            record = self.model().query.order_by(self.model.id).all()
            response = [user.toJson() for user in record]
            return response, 200
        
        except Exception as e:
            return {
                'errors': str(e)
            }, 500

    def create(self, json):
        try:
            user = CrearUserSchema(**json)
            user.password = self.__hashPassword(user.password)
            record = self.model(**user.model_dump())
            
            db.session.add(record)
            db.session.commit()
            return record.toJson(), 201
        
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
            record = self.model().query.get(id)

            if record is None:
                raise Exception('User not found')
            
            user = UpdateUserSchema(**json)

            if user.password is not None:
                user.password = self.__hashPassword(user.password)
            
            record.update(user)
            db.session.commit()
            return record.toJson(), 200
        
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
            record = self.model().query.get(id)

            if record is None:
                raise Exception('User not found')
            
            db.session.delete(record)
            db.session.commit()
            return {
                'message': 'User deleted successfully'
            }, 200
        
        except Exception as e:
            return {
                'errors': str(e)
            }, 500

    def getById(self, id: int):
        try:
            record = self.model().query.get(id)

            if record is None:
                raise Exception('User not found')
            
            return record.toJson(), 200
        
        except Exception as e:
            return {
                'errors': str(e)
            }, 500

    def __hashPassword(self, password):
        pwdBytes = password.encode('utf-8')
        pwdHash = bcrypt.hashpw(pwdBytes, bcrypt.gensalt())
        return pwdHash.decode()