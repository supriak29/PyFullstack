# from multiprocessing import connection
# from os import curdir
from dbConfig import DatabaseConfig

# 'data' is the database name we are passing
connection, cursor = DatabaseConfig('data').createConnection()

# creating a table having cols - id, username, password
createTable = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,username text, password text)"
cursor.execute(createTable)
