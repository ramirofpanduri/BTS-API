from services.book_service import fetch_all_books, fetch_book_by_id, fetch_books_by_category


def get_all_books():
    books = fetch_all_books()
    if books is None or len(books) == 0:
        return {"error": "No book found"}, 404
    return {"books": books}, 200


def get_book_by_id(book_id):
    book = fetch_book_by_id(book_id)
    if book is None:
        return {"error": "No book found"}, 404
    return {"book": book}, 200


def get_books_by_category(category_id):
    books = fetch_books_by_category(category_id)
    if books is None or len(books) == 0:
        return {"error": "No book found in this category"}, 404
    return {"books": books}, 200
