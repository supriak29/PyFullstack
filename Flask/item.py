from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)  
api = Api(app) 

items = []

class Item(Resource):
	
    # def get(self,name):
	# 	# to get a particular item from list
    #     # check if the item is present
	# 	for item in items:
    #         if item['name']==name:
    #             return item
    #     return 'message': 'no such item in the list'
    #         # pick an item from list, 
    #         # check if it matches from the one requeted
    #         # item['name'] - item name from list
    #         # name - requested from user
    def get(self,name):
        for item in items:
            if item['name']==name:
                return item
        return {'message':'No item in the list'}
            
    # post is used to create something/item
    def post(self,name):
        # creating a static item name and default price as 120
        item = {'name':name, 'price':12.00}
        # add the newly added item into items list at the end using append
        items.append(item)
        return items


api.add_resource(Item,'/item/<string:name>') # http:127.0.0.1:5000/item/<itemName>
app.run(port=5000, debug=True)

##########################################

# ***   POSTMAN ***

# POST: {{url}}/item/sugar
# here, item name sugar with with default price 12.0 gets appended in list

# GET: {{url}}/item/sugar


