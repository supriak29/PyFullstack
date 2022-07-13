import hmac
from user import User

# users = [ 
#     User(1, 'user1','pass1') 
# ]

# # mapping through username
# username_mapping = {u.username: u for u in users}
# # mapping through user id
# userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    #user = username_mapping.get(username,None)
    #if user and user.password==password:
    user = User.findUsername(username)
    if user and hmac.compare_digest(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.findId(user_id)