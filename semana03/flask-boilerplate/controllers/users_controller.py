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
            record = self.model().query.all()
            response = [user.toJson() for user in record]
            return response, 200
        
        except Exception as e:
            return {
                'errors': str(e)
            }

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
            }
        except Exception as e:
            db.session.rollback()
            return {
                'errors': str(e)
            }
    
    def update(self, id, json):
        try:
            record = self.model().query.get(id)

            if record is None:
                raise Exception('User not found')
            
            user = UpdateUserSchema(**json)

            if user.password is not None:
                user.password = self.__hashPassword(user.password)
            
            record.update(user)
            db.session.commit()

            return {
                'ok': True
            }
        except ValidationError as e:
            return {
                'errors': e.errors()
            }
        except Exception as e:
            db.session.rollback()
            return {
                'errors': str(e)
            }

    def delete(self):
        pass

    def getById(self):
        # Logica para retornar un usuario por id
        pass

    def __hashPassword(self, password):
        pwdBytes = password.encode()
        pwdHash = bcrypt.hashpw(pwdBytes, bcrypt.gensalt())
        return pwdHash.decode()