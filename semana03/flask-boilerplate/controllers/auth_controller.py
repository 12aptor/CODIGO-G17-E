from models.users_model import UserModel
from schemas.users_schema import LoginUserSchema
from pydantic import ValidationError
import bcrypt
from flask_jwt_extended import create_access_token, create_refresh_token

class AuthController:
    def __init__(self) -> None:
        self.model = UserModel

    def login(self, json):
        try:
            user = LoginUserSchema(**json)
            record = self.model.query.filter_by(email=user.email).first()

            if record is None:
                raise Exception('Invalid credentials')
            
            pwdBytes = user.password.encode('utf-8')
            checkPwd = bcrypt.checkpw(pwdBytes, record.password.encode('utf-8'))

            if not checkPwd:
                raise Exception('Invalid credentials')

            accessToken = create_access_token(identity=record.id, additional_claims={'ok': True})
            refreshToken = create_refresh_token(identity=record.id)

            return {
                'access_token': accessToken,
                'refresh_token': refreshToken,
            }, 200

        except ValidationError as e:
            return {
                'errors': e.errors()
            }, 400
        except Exception as e:
            return {
                'errors': str(e)
            }, 500
