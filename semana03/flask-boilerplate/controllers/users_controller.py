from models.users_model import UserModel
from db import db

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
        record = self.model(
                    name=json['name'],
                    document_type=json['document_type'],
                    document_number=json['document_number'],
                    email=json['email'],
                    password=json['password'],
                    status=json['status']
                )
        
        db.session.add(record)
        db.session.commit()

        return record.toJson(), 201
    
    def update(self):
        pass

    def delete(self):
        pass

    def __hashPassword(self):
        pass