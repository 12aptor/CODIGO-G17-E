from models.users_model import UserModel
from db import db
from pydantic import ValidationError
from schemas.users_schema import UserSchema
import bcrypt

class UserController:
    def __init__(self):
        self.model = UserModel

    def getAll(self):
        record = self.model().query.all()

        response = []
        for user in record:
            response.append(user.toJson())

        return response, 200

    def getById(self):
        # Logica para retornar un usuario por id
        pass

    def create(self, json):
        try:
            user = UserSchema(**json)
            user.password = self.__hashPassword(user.password)
            record = self.model(**user.__dict__)
            
            db.session.add(record)
            db.session.commit()
            return record.toJson(), 201
        
        except ValidationError as e:
            return {
                'errors': e.errors()
            }
        except Exception as e:
            return {
                'errors': e.args
            }
    
    def update(self):
        pass

    def delete(self):
        pass

    def __hashPassword(self, password):
        pwdBytes = password.encode()
        pwdHash = bcrypt.hashpw(pwdBytes, bcrypt.gensalt())
        return pwdHash.decode()