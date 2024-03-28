from flask import Blueprint, request
from controllers.users_controller import UserController


api_bp = Blueprint('api', __name__)

@api_bp.route('/users/all')
def getAllUsers():
    controller = UserController()
    return controller.getAll()

@api_bp.route('/users/create', methods=['POST'])
def createUser():
    json = request.get_json()
    controller = UserController()
    return controller.create(json)