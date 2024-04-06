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