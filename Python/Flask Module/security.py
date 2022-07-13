from user import User

users = [ 
    User(1, 'user1','pass1') 
]

# mapping through username
username_mapping = {u.username: u for u in users}

# mapping through user id
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username,None)
    if user and user.password==password:
        return user

user_id=0

def identity(payload):
    user_id == payload['identity']
    return userid_mapping.get(user_id, None)