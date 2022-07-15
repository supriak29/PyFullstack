import hmac
from modules.user import UserModule

# users = [ 
#     User(1, 'user1','pass1') 
# ]

# # mapping through username
# username_mapping = {u.username: u for u in users}

# # mapping through user id
# userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    #user = username_mapping.get(username,None)  # if the username is not there after checking usermapping, then None is assigned to user 
    #if user and user.password==password: 
    user = UserModule.findUsername(username)
    if user and hmac.compare_digest(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModule.findId(user_id)