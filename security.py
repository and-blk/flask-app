from user import User
# from flask_jwt import JWT, jwt_required
# from app import app

users = [
    User(1, "Andrey", "qwerty"),
    User(2, "Sanya", "asdf")
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)


