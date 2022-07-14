"""
    This main.py file is the main file for the project.
    The server starts from here. All the endpoints are registered in this file.
    This file helps in routing the incoming api request to the appropriate resource.
    This file has all the main imports required to create the server.
"""

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from user import RegisterUser
from security import authenticate, identity
from weather import Weather, WeatherList




app = Flask(__name__)  # object of flask created
app.secret_key = 'supriya'
api = Api(app)  # object of API created


jwt = JWT(app, authenticate, identity)




api.add_resource(Weather,'/weather')
api.add_resource(WeatherList,'/weather/records')
# api.add_resource(RegisterUser,'/register') 
api.add_resource(RegisterUser,'/user/register')

# print("This is from main.py: ",__name__)


if __name__ == '__main__':
    # app.run(port=5000) # here, debug is off. it won't show us errors if any
    app.run(port=5000, debug=True) # we want to see errors if any, therefore debug=True

