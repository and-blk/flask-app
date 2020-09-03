from flask_restful import Resource
from flask import request
from flask_jwt import jwt_required

items = []




class Item(Resource):

    @jwt_required
    def get(self, name):
        for item in items:
            if item["name"] == name:
                return item, 200
        return {"item": None}, 404


    def post(self, name):
        data = request.get_json()
        item = {"name": name, "price": data["price"]}
        items.append(item)
        return item, 201


class ItemList(Resource):
    #@jwt_required
    def get(self):
        return {"items": items}