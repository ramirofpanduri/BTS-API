from database.db import get_db_connection


def fetch_all_categories():
    conn = get_db_connection()
    if not conn:
        return None

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM categories ORDER BY id ASC")
    books = cursor.fetchall()
    cursor.close()
    return books


def fetch_category_by_id(categories_id):
    conn = get_db_connection()
    if not conn:
        return None

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM categories WHERE id = %s", (categories_id,))
    book = cursor.fetchone()
    cursor.close()
    return book
