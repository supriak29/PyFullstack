import hmac
from user import User


def authenticate(username, password):
    user = User.findUsername(username)
    if user and hmac.compare_digest(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.findId(user_id)