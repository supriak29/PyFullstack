# from multiprocessing import connection
import sqlite3

class DatabaseConfig:
    def __init__(self, databaseName=None):
        self.databaseName = databaseName
    
    def createConnection(self):
        databaseName = '.'.join((str(self.databaseName),'db')) # db here is the extension we are providing our database file name
        print(databaseName) # prints the database name along with extension
        connection = sqlite3.connect(databaseName)  # connect with database
        cursor = connection.cursor() # create connection with cursor
        return connection, cursor  

    def commitClose(self):   # commiting the changes & closing the connection
        connection, cursor = self.createConnection() 
        connection.commit()
        connection.close()
