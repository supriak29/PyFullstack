"""
    This main.py file is the main file for the project.
    The server starts from here. All the endpoints are registered in this file.
    This file helps in routing the incoming api request to the appropriate resource.
    This file has all the main imports required to create the server.
"""

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from user import RegisterUser
from security import authenticate, identity
from weather import Weather, WeatherList




app = Flask(__name__)  # object of flask created
app.secret_key = 'supriya'
api = Api(app)  # object of API created


jwt = JWT(app, authenticate, identity)

# weather.py
# class Weather
# class WeatherList


api.add_resource(Weather,'/weather')                # 127.0.0.1:5000/weather
api.add_resource(WeatherList,'/weather/records')    # {{url}}/weather/records
api.add_resource(RegisterUser,'/user/register')     # {{url}}/user/register


if __name__ == '__main__':
    # app.run(port=5000) # here, debug is off. it won't show us errors if any
    app.run(port=5000, debug=True) # we want to see errors if any, therefore debug=True

