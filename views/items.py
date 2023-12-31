from flask import Blueprint

items_app = Blueprint(
    "items_app",
    __name__,
    url_prefix="/items"
)


@items_app.get("/")
def get_items_list():
    return {
        "data": [
            {
                "id": 1,
                "name": "foobar",
            },
            {
                "id": 2,
                "name": "fizzbuzz",
            },
        ]
    }


def get_item_by_id_logic(item_id):
    return {"data": {"id": item_id}}


@items_app.get("/<int:item_id>/")
def get_item_by_id(item_id: int):
    return get_item_by_id_logic(item_id)
