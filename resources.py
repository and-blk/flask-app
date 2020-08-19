from flask_restful import Resource

items = []

class Item(Resource):
    def get(self, name):
        items.append({"item": name})
        return items
