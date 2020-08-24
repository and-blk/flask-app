from flask_restful import Resource
from flask import request
from security import authenticate, identity
from flask_jwt import JWT, jwt_required


from app import app

jwt = JWT(app, authenticate, identity)

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
    def get(self):
        return {"items": items}