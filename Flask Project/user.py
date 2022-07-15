from flask_restful import Resource, reqparse
import sqlite3
from dbConfig import DatabaseConfig

###########################################################################

# has no direct link with API
class User:
    def __init__(self, _id, username, password):
        # initializing instance variables (self.id, self.username, self.password) of class User
        self.id = _id   
        self.username = username
        self.password = password
    
    # finding through username
    @classmethod
    def findUsername(cls, username):
        connection = sqlite3.connect('weatherDB.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users_cred WHERE username=?"
        result = cursor.execute(query,(username,))
        row = result.fetchone()
        if row: 
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
        connection = sqlite3.connect('weatherDB.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users_cred WHERE id=?"
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
class RegisterUser(Resource):

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
        data = RegisterUser.parser.parse_args()
    
        if User.findUsername(data['username']):
            return {"message": "A user with current username already exists!"}, 400
        
        connection, cursor = DatabaseConfig('weatherDB').createConnection()
        
        # since id is primary key, it will auto increment, therefore we send null right now
        query = "INSERT INTO  users_cred VALUES(NULL, ?, ?)" 
        cursor.execute(query, (data['username'], data['password']))

        #DatabaseConfig.commitClose()
        connection.commit()
        connection.close()
        return {"message": "User created successfully!"}, 201

    def get(self):
        connection, cursor = DatabaseConfig('weatherDB').createConnection()
        
        query = "SELECT * FROM users_cred"
        result = cursor.execute(query)
    
        users = []
        for row in result:
            users.append( {  
                               'username':row[1],
                               'password': row[2]
                    }
                )

        connection.close()
        return {'Registered Users': users}