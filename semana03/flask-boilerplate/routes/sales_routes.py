from flask import Blueprint, request
from controllers.sales_controller import SaleController


sales_bp = Blueprint('sales', __name__)

@sales_bp.route('/sales/create', methods=['POST'])
def createSale():
    json = request.get_json()
    controller = SaleController()
    return controller.create(json)

@sales_bp.route('/sales/all', methods=['GET'])
def getAllSales():
    controller = SaleController()
    return controller.getAll()