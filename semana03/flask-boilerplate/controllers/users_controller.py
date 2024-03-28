from models.users_model import UserModel

class UserController:
    def __init__(self):
        self.model = UserModel()

    def getAll(self):
        # Logica para retornar todos los usuarios
        pass

    def getById(self):
        # Logica para retornar un usuario por id
        pass

    def create(self):
        pass
    
    def update(self):
        pass

    def delete(self):
        pass

    def __hashPassword(self):
        pass