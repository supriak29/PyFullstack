from dbConfig import DatabaseConfig

# 'data' is the database name we are passing
connection, cursor = DatabaseConfig('data').createConnection()

# creating a user table
createTable = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,username text, password text)"
cursor.execute(createTable)

# creating items table
createTable = "CREATE TABLE IF NOT EXISTS items(name text, price float)"
cursor.execute(createTable)

#cursor.execute("INSERT INTO weather_stats VALUES('India','Mumbai','Light Drizzle','95%', '27°C', '94%','18km/h')")

connection.commit()
connection.close()

#############################
# country
# city
# weather stats - metric
# temp °C
# humidity %
# precipitation %
# wind %
