#from typing_extensions import Required
from flask_restful import Resource, reqparse
#from multiprocessing import connection
#from sqlite3 import connect
import sqlite3
from dbConfig import DatabaseConfig

#from colorama import Cursor

###########################################################################

# has no direct link with API
class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    # finding through username
    @classmethod
    def findUsername(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query,(username,))
        row = result.fetchone()
        if row: # if there is data then:
            #user = cls(row[0],row[1],row[2])
            user = cls(*row) # will take entire single row - *args
        else:
            user = None
        
        connection.close()
        return user

    # finding through id
    @classmethod
    def findId(cls, _id):
        print("This is id: ",_id)
        print("This is type of id: ",type(_id))
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query,(_id,))
       # result = cursor.execute(query,_id)
        row = result.fetchone() # fetchone gives a tuple(one row)
        if row: 
            user = cls(*row) 
            print('This is the user from database: ',user)
        else:
            user = None

        
        connection.close()
        return user


############################################################################

# this class will have direct link with API
class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
                'username',
                type=str,
                required=True,
                help='This field is required!'
            )
    parser.add_argument(
                'password',
                type=str,
                required=True,
                help='This field is required!'
            )

    # create something
    def post(self):
        data = UserRegister.parser.parse_args()
        print("This is from UserRegister class post method: ",data)
        
        
        if User.findUsername(data['username']):
            return {"message": "A user with current username already exists!"}, 400
        
        databaseName = 'data'
        connection, cursor = DatabaseConfig(databaseName).createConnection()
        
        # since id is primary key, it will auto increment, therefore we send null right now
        query = "INSERT INTO  users VALUES(NULL, ?, ?)" 
        cursor.execute(query, (data['username'], data['password']))

        #DatabaseConfig.commitClose()
        connection.commit()
        connection.close()
        return {"message": "User created successfully!"}, 201