from flask import Blueprint, request
from controllers.products_controller import ProductController
from flask_jwt_extended import jwt_required


products_bp = Blueprint('products', __name__)

@products_bp.route('/products/create', methods=['POST'])
@jwt_required()
def createProduct():
    json = request.get_json()
    controller = ProductController()
    return controller.create(json)

@products_bp.route('/products/all')
def getAllProducts():
    controller = ProductController()
    return controller.getAll()

@products_bp.route('/products/update/<int:id>', methods=['PUT'])
def updateProduct(id):
    json = request.get_json()
    controller = ProductController()
    return controller.update(id, json)

@products_bp.route('/products/delete/<int:id>', methods=['DELETE'])
def deleteProduct(id):
    controller = ProductController()
    return controller.delete(id)

@products_bp.route('/products/<int:id>')
def getById(id):
    controller = ProductController()
    return controller.getById(id)