"""
    This main.py file is the main file for the project.
    The server starts from here. All the endpoints are registered in this file.
    This file helps in routing the incoming api request to the appropriate resource.
    This file has all the main imports required to create the server.
"""


from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from user import UserRegister
from security import authenticate, identity
from items import Item, ItemList




app = Flask(__name__)  # object of flask created
app.secret_key = 'supriya'
api = Api(app)  # object of API created


jwt = JWT(app, authenticate, identity)




#api.add_resource(Item,'/item/<string:name>') # http://127.0.0.1:5000/student/Supriya
api.add_resource(Item,'/item')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register') 


if __name__ == '__main__':
    # app.run(port=5000) # here, debug is off. it won't show us errors if any
    app.run(port=5000, debug=True) # we want to see errors if any, therefore debug=True

