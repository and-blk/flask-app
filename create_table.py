import sqlite3

connection = sqlite3.connect("web_app_sqllite3.db")

cursor = connection.cursor()
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_item_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_item_table)

connection.commit()
connection.close()