from flask import Flask, jsonify, request
from flask_restful import Api
import resources

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)

api.add_resource(resources.Item, '/item/<string:name>')

app.run(host='0.0.0.0', port=5000)
