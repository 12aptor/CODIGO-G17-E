from flask import Blueprint, request
from controllers.users_controller import UserController
from flask_jwt_extended import jwt_required


user_bp = Blueprint('user', __name__)

@user_bp.route('/users/all')
@jwt_required()
def getAllUsers():
    controller = UserController()
    return controller.getAll()

@user_bp.route('/users/create', methods=['POST'])
def createUser():
    json = request.get_json()
    controller = UserController()
    return controller.create(json)

@user_bp.route('/users/update/<int:id>', methods=['PUT'])
def updateUser(id):
    json = request.get_json()
    controller = UserController()
    return controller.update(id, json)

@user_bp.route('/users/delete/<int:id>', methods=['DELETE'])
def deleteUser(id):
    controller = UserController()
    return controller.delete(id)

@user_bp.route('/users/by-id/<int:id>')
def getUserById(id):
    controller = UserController()
    return controller.getById(id)

@user_bp.route('/users/by-name/<string:name>')
def getUserByName(name):
    controller = UserController()
    return controller.getByName(name)