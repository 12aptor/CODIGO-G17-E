from flask import Blueprint, request
from controllers.auth_controller import AuthController

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/login', methods=['POST'])
def login():
    json = request.get_json()
    controller = AuthController()
    return controller.login(json)