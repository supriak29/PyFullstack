"""
    This file performs CRUD operations.
    Create - using post() method
    Retrieve - using get() method
    Update - using put() method
    Delete - using delete() method
"""

# imports 
from dbConfig import DatabaseConfig
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Weather(Resource):
    ''''
        This class is used for CRUD operations on single city value
    '''
    parser = reqparse.RequestParser()

    parser.add_argument(
        'city',
        type=str,
        required=True, 
        help='This field is required'
    )
    parser.add_argument(
        'country',
        type=str,
        required=False,
        help='This field is optional'
    )

    # check if the record for single city is present and return if present
    def get(self):
        ''''
            This method fetches a single record on the basis of city requested by the user.
            This get() method shows the fetched data, depending on the city
        '''
        data = Weather.parser.parse_args()       # taking the request through parser, weather stats for a city
        wstat = self.findItem(data['city'])      # find if the required city is there in database    
        if wstat:                                # if the city is found: 
            return wstat                         # then return details regarding the requested city
        return {'message': 'Search not found'}, 404     # else return message
   
   
    @classmethod                 # class method can be accessed throughout the class anywhere, unlike post,get,delete,update methods
    def findItem(cls, city):     # takes city as parameter
        '''
            This function searches/finds if the requested city is there in database.
            If present then select that row and return it
            else function returns None
        '''
        connection, cursor = DatabaseConfig('weatherDb').createConnection()     # connecting to database
        query = "SELECT * FROM weather_stats WHERE city=?"                      # select query
        result = cursor.execute(query, (city,))                                 # execute select query
        row = result.fetchone()                                                 # fetch that one row and store in row
        connection.close()                                                      # close connection

        if row:                                             # if the city exists then row won't be empty
            return{ "weather":{                             # return row in systematic way in the form of dictionary
                                'country': row[0],
                                'city': row[1],
                                'metric': row[2],
                                'humidity':row[3],
                                'temperature':row[4],
                                'precipitation':row[5],
                                'wind': row[6],
                                'uvindex': row[7],
                                'sunrise': row[8],
                                'sunset': row[9],
                                'day': row[10], 
                                'date': row[11]  
                              }
                    }
    
    @classmethod
    def insert(cls, wstat):
        '''
            This function is to insert into database as per the request.
        '''
        connection, cursor = DatabaseConfig('weatherDB').createConnection()                 # connect to database
        query = "INSERT INTO  weather_stats VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"     # insert query
        cursor.execute(query, (                                                             # execute insert query
                                wstat['country'], wstat['city'], wstat['metric'],
                                wstat['humidity'], wstat['temperature'], wstat['precipitation'], 
                                wstat['wind'], wstat['uvindex'], wstat['sunrise'], wstat['sunset'],
                                wstat['day'], wstat['date']
                            )  
                        )
        connection.commit()         # commit the changes
        connection.close()          # close connection

    @classmethod
    def update(cls, wstat):
        '''
            This method is used to update data in database.
            It takes parameter: wstat
            Using the parameters receieved through request, we update database in this method
        '''
        connection, cursor = DatabaseConfig('weatherDB').createConnection()     # connect to db
        query = """ UPDATE weather_stats                                        
                    SET metric=?, humidity=?, temperature=?, precipitation=?, 
                        wind=?, uvindex=?, sunrise=?, sunset=?, day=?, date=?
                    WHERE city=? 
                """                                                             #update query
        cursor.execute(query, (                                                 # execute the update query        
                                wstat['metric'], wstat['humidity'], wstat['temperature'],
                                wstat['precipitation'], wstat['wind'],
                                wstat['uvindex'], wstat['sunrise'], wstat['sunset'],
                                wstat['day'], wstat['date'], wstat['city']
                            )
                    )
        connection.commit() # commit changes
        connection.close()  # close connection


    @jwt_required()
    def post(self):
        ''''
            This method creates a new record into database.
            It uses insert query which is inherited from classmethod insert()
            
            In this method, request is taken through .get_json() instead of parse.
            Reason: parse allows only 2 arguments in this case: country & city
                  :  we need more than 2 parameteres,
                  :  to avoid too many loc 
        '''
        data = request.get_json()   

        if self.findItem(data['city']):     # find if the city is present in the database
            # if city found in db, then we do not have to again post into db
            return {'message':"Data for city with name '{}' already exists.".format(data['city'])}, 400
        
        
        # creating an object: wstat
        wstat = {
                'country': data['country'],
                'city': data['city'],
                'metric': data['metric'],
                'humidity':  data['humidity'],
                'temperature': data['temperature'],
                'precipitation': data['precipitation'],
                'wind': data['wind'],
                'uvindex': data['uvindex'],
                'sunrise': data['sunrise'],
                'sunset': data['sunset'],
                'day': data['day'], 
                'date': data['date']
        }
        
        try:
            # calling the class method insert
            self.insert(wstat)
            return {"message": "Record Updated!"}
        except:
            return{"message": "An error occurred while inserting item"}, 500
        


    @jwt_required()
    def delete(self):
        '''
            This method deletes a record from database if any, using city.
        '''
        connection, cursor = DatabaseConfig('weatherDB').createConnection()
        data =  Weather.parser.parse_args()
        
        if self.findItem(data['city']):                         # check if requested city exists in db
            query = "DELETE FROM weather_stats WHERE city=?"    # delete it's record if exists
            cursor.execute(query, (data['city'],))              # execute the query
            connection.commit()                                 # commit the changes
            connection.close()                                  # close connection
            return {"message": "Weather report for city {} deleted from database".format(data['city'])}
        return {"message": "City requested to be deleted does not exist in the database"}

    
    # # update list
    @jwt_required()
    def put(self):
        ''''
            This method is for updating and appending purpose.
            For updating in db we use update query whereas for appending we use insert query.
            We have created seperated classmethods for both operations which can be called in this method
        '''
        data =  request.get_json()

        wstat = {
               'country': data['country'],
                'city': data['city'],
                'metric': data['metric'],
                'humidity':  data['humidity'],
                'temperature': data['temperature'],
                'precipitation': data['precipitation'],
                'wind': data['wind'],
                'uvindex': data['uvindex'],
                'sunrise': data['sunrise'],
                'sunset': data['sunset'],
                'day': data['day'], 
                'date': data['date']
        }
        
        if self.findItem(data['city']):
            try:
                self.update(wstat)
                return {"message": "Database updated"}
            except:
                return{"message": "An error occurred while inserting report"}, 500
        else:
            try:
                self.insert(wstat)
                return {"message": "Database updated"}
            except:
                return{"message": "An error occurred while inserting item"}, 500



class WeatherList(Resource):
    ''''
        This class displays all the weather records from database: weatherDB
    '''
        
    def get(self):
        connection, cursor = DatabaseConfig('weatherDB').createConnection()
        
        query = "SELECT * FROM weather_stats"
        result = cursor.execute(query)
    
        wstat = []
        for row in result:
            wstat.append( {  
                                'country':row[0], 'city':row[1],'metric':row[2], 'humidity':row[3],
                                'temperature':row[4],'precipitation':row[5], 'wind':row[6],
                                'uvindex':row[7], 'sunrise':row[8], 'sunset':row[9],
                                'day':row[10], 'date':row[11]
                    }
                )

        connection.close()
        return {'Weather Stats': wstat}