from flask import Flask
from flask_restful import Api
#import resources
from security import identity, authenticate
from flask_jwt import JWT, jwt_required
from flask_restful import Resource
from flask import request





app = Flask(__name__)
app.config.from_object('config')
api = Api(app)

items = []



class Item(Resource):

    # @jwt_required
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
    @jwt_required
    def get(self):
        return {"items": items}




api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

jwt = JWT(app, authenticate, identity)

app.run(host='0.0.0.0', port=5000)