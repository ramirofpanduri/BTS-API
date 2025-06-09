from flask import Blueprint, jsonify
from controllers.book_controllers import get_all_books, get_book_by_id, get_books_by_category

books_bp = Blueprint('books', __name__)


@books_bp.route('/books', methods=['GET'])
def all_books():
    response, status_code = get_all_books()
    return jsonify(response), status_code


@books_bp.route('/books/<int:book_id>', methods=['GET'])
def book_by_id(book_id):
    response, status_code = get_book_by_id(book_id)
    return jsonify(response), status_code


@books_bp.route("/books/category/<int:category_id>", methods=["GET"])
def books_by_category(category_id):
    response, status_code = get_books_by_category(category_id)
    return jsonify(response), status_code
