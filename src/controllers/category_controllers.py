from services.category_service import fetch_all_categories, fetch_category_by_id


def get_all_categories():

    return fetch_all_categories()


def get_category_by_id(category_id):

    return fetch_category_by_id(category_id)
