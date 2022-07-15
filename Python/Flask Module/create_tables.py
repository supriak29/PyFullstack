from dbConfig import DatabaseConfig

# 'data' is the database name we are passing
connection, cursor = DatabaseConfig('data').createConnection()

# creating a user table
createTable = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,username text, password text)"
cursor.execute(createTable)

# creating items table
createTable = "CREATE TABLE IF NOT EXISTS items(name text, price float)"
cursor.execute(createTable)

connection.commit()
connection.close()

