from flask import Flask, jsonify, request

app = Flask(__name__)
app.config.from_object('config')
stores = [
    {
        "name": "Andrey store",
        "items": [
            {
                "name": "lantern",
                "price": 20.00
            }
        ]
    }
]

@app.route('/store')
def get_stores():
    return jsonify({"stores": stores})


@app.route('/store', methods=['POST'])
def create_new_store():
    request_data = request.get_json()
    stores.append({"name": request_data["name"],
                   "items": []})
    return jsonify({"stores": stores})


@app.route('/store/<string:name>')
def search_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message": "no such store"})


@app.route('/store/<string:name>/item')
def search_store_item(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store["items"])
    return jsonify({"message": "no such store"})


@app.route('/store/<string:name>/item', methods=['POST'])
def add_item(name):
    request_data = request.get_json()
    for store in stores:
        if name == store["name"]:
            store["items"].append(request_data)
            return jsonify(stores)
    return jsonify({"message": "no such store"})



app.run(host="0.0.0.0", port=5000)