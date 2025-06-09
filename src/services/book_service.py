from database.db import get_db_connection


def fetch_all_books():
    conn = get_db_connection()
    if not conn:
        return None

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books ORDER BY id ASC")
    books = cursor.fetchall()
    cursor.close()
    return books


def fetch_book_by_id(book_id):
    conn = get_db_connection()
    if not conn:
        return None

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    cursor.close()
    return book


def fetch_books_by_category(category_id):
    conn = get_db_connection()
    if not conn:
        return None

    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM books WHERE category_id = %s ORDER BY id ASC",
        (category_id,)
    )
    books = cursor.fetchall()
    cursor.close()
    return books
