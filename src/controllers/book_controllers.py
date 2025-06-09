from services.book_service import fetch_all_books, fetch_book_by_id


def get_all_books():

    return fetch_all_books()


def get_book_by_id(book_id):

    return fetch_book_by_id(book_id)
