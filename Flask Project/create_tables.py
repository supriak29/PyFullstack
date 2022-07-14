from dbConfig import DatabaseConfig

# 'weatherDB' is the database name we are passing
connection, cursor = DatabaseConfig('weatherDB').createConnection()

# creating a user table
createTable = "CREATE TABLE IF NOT EXISTS users_cred(id INTEGER PRIMARY KEY,username text, password text)"
cursor.execute(createTable)

# creating weather_stats table
createTable = """   CREATE TABLE IF NOT EXISTS weather_stats(
                        country text, city text, metric text, humidity text, 
                        temperature text, precipitation text, wind text, 
                        uvindex text, sunrise text, sunset text,
                        day text, date text)
            """
cursor.execute(createTable)

connection.commit()
connection.close()

#############################

# country
# city
# weather stats - metric
# temp °C
# feels like
# humidity %
# precipitation %
# wind %
# wind direction
# uv index
# sunrise
# sunset