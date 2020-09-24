from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",
                        type=float,
                        required=True,
                        help="This field can't be blank!")


    def get(self, name):
        item = self.find_item(name)
        if item:
            return {"item": item}
        return {"message": f"There is no item {name}"}


    @classmethod
    def find_item(cls, name):
        connection = sqlite3.connect('web_app_sqllite3.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name=?"

        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return row
        return None


    def post(self, name):
        if self.find_item(name):
            return {"message": f"item {name} already exists!"}

        data = Item.parser.parse_args()
        item = {"name": name, "price": data["price"]}

        try:
            self.insert(item)
        except Exception as e:
            return {"message": "internal server error occurred in insertion", "error": str(e)}, 500

        return item, 201

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('web_app_sqllite3.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES (?,?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()


    def delete(self, name):
        item = {"name": name}
        connection = sqlite3.connect('web_app_sqllite3.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (item['name'],))

        connection.commit()
        connection.close()

        return {"message": f"item {item['name']} has been deleted"}


    def put(self, name):
        data = Item.parser.parse_args()
        item = self.find_item(name)
        updated_item = {"name": name, "price": data["price"]}

        if item:
            try:
                self.update(updated_item)
                return {"message": f"item {name} has been updated"}
            except Exception as e:
                return {"message": f"error during updating item {name}", "error": str(e)}
        else:
            try:
                self.insert(updated_item)
                return {"message": f"item {name} has been added to DB"}
            except Exception as e:
                return {"message": f"error during inserting item {name}",  "error": str(e)}


    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('web_app_sqllite3.db')
        cursor = connection.cursor()
        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item["price"], item["name"],))

        connection.commit()
        connection.close()


class ItemList(Resource):
    @jwt_required()
    def get(self):
        connection = sqlite3.connect('web_app_sqllite3.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"

        result = cursor.execute(query)
        items = result.fetchall()
        connection.close()

        if items:
            return {"items": items}
        return None