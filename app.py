from flask import Flask, jsonify
from flask_restful import Api
import resources
from security import identity, authenticate
from flask_jwt import JWT, jwt_required
from flask_restful import Resource
from flask import request
from user import User




app = Flask(__name__)
app.config.from_object('config')
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(resources.Item, '/item/<string:name>')
api.add_resource(resources.ItemList, '/items')



app.run(host='0.0.0.0', port=5000)