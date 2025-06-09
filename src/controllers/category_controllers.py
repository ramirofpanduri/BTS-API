from services.category_service import fetch_all_categories, fetch_category_by_id


def get_all_categories():
    categories = fetch_all_categories()
    if categories is None or len(categories) == 0:
        return {"error": "No category found"}, 404
    return {"categories": categories}, 200


def get_category_by_id(category_id):
    category = fetch_category_by_id(category_id)
    if category is None:
        return {"error": "No category found"}, 404
    return {"category": category}, 200
