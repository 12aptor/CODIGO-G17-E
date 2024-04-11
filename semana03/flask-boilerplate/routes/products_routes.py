from flask import Blueprint, request
from controllers.products_controller import ProductController
from flask_jwt_extended import jwt_required, get_jwt_identity


products_bp = Blueprint('products', __name__)

@products_bp.route('/products/create', methods=['POST'])
@jwt_required()
def createProduct():
    current_user = get_jwt_identity()
    if(current_user['role'] != 'ADMIN'):
        return {
            'msg': 'Unauthorized'
        }, 401
    
    json = request.get_json()
    controller = ProductController()
    return controller.create(json)

@products_bp.route('/products/all')
def getAllProducts():
    controller = ProductController()
    return controller.getAll()

@products_bp.route('/products/update/<int:id>', methods=['PUT'])
@jwt_required()
def updateProduct(id):
    json = request.get_json()
    controller = ProductController()
    return controller.update(id, json)

@products_bp.route('/products/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteProduct(id):
    controller = ProductController()
    return controller.delete(id)

@products_bp.route('/products/by-id/<int:id>')
def getById(id):
    controller = ProductController()
    return controller.getById(id)