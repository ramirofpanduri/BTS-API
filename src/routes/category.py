from flask import Blueprint, jsonify
from controllers.category_controllers import get_all_categories, get_category_by_id

categories_bp = Blueprint('categories', __name__)


@categories_bp.route('/categories', methods=['GET'])
def all_categories():
    response, status_code = get_all_categories()
    return jsonify(response), status_code


@categories_bp.route('/categories/<int:category_id>', methods=['GET'])
def category_by_id(category_id):
    response, status_code = get_category_by_id(category_id)
    return jsonify(response), status_code
