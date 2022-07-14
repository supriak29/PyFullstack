from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__) # created object of flask 
api = Api(app) # creating object of API

stud = []

# when we talk talk about resources & api representing resources,
# we mean to create a class
# previously we saw function based API
# Now, we will create class based API

# class Student inherts from Resource, 
# therefore, my Student becomes my Resource
# and so my API should call resource i.e., Student in this case
class Student(Resource):
    # get method - when a particular name of a student is given,
    # it should return the name of the student
    # def get(self, name):
    #     return {'student':name}
      def get(self):
        name = request.get_json()
        return name

      def post(self):
        name = request.get_json()
        stud.append(name)
        return {'message': 'Student added into list'}

class AllStudents(Resource):
  def get(self):
    return stud


    

# calling the above class:
#api.add_resource(Student,'/student/<string:name>') # http:127.0.0.1:5000/student/Supriya
api.add_resource(Student,'/student')
api.add_resource(AllStudents,'/students')


# my app should run on port no. 5000
app.run(port=5000,debug=True)

################################################################3

# EXECUTE THIS MODULE:

# **** CMD **** get into virtual environment
# > Scripts/activate
# > py student.py

# **** POSTMAN ****
# create "Resource Student" Folder
# Add request - Get Student Name
# {{url}}/student/Supriya
 
####################################################################

# The above code will return empty list as we did not add 
# anything in it, we have just asked the server to fetch data


    

	