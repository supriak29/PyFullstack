import sqlite3


# has no direct link with API
class UserModule:
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
