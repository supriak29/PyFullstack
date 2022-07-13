from ast import parse
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from pkg_resources import require


from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'supriya'
api = Api(app)


jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
    # check if the single item is present and return if present
    #@jwt_required()
    def get(self):
        data = request.get_json()
        item = next( filter(lambda x: x['name']==data['name'], items), None)
        return {'item':item}, 200 if item else 404
##        for item in items:
##            if item['name'] == name:
##                return item
##       return {'item': 'No item in the store'}, 404 # status 404 - error
                
    # create an item, insert into list of items and return list of all items
    def post(self):
        data = request.get_json() # json gets converted into dictionary
        if next(filter(lambda x: x['name']== data['name'], items), None):
            return {'message':"An item with name '{}' already exists.".format(data['name'])}, 400
        else:
            # print(data)
            item = {'name':data['name'],'price':data['price']}
            #item = {'name':name,'price':12.00} # static
            items.append(item)
            return items, 201 # status 201, creating something

    def delete(self):
        # trying to access global variable in local scope
        global items
        data = request.get_json() # taking input from user
        items = list(filter(lambda x: x['name'] != data['name'], items))
        return {'message':'Item deleted'}
    
    # update list
    def put(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument(
        #                         'price',
        #                         type=float,
        #                         required=True,
        #                         help="This is required!"
        #                     )
        # parser.add_argument(
        #                         'name',
        #                         type=str,
        #                         required=True,
        #                         help="This is required!"
        #                     )
        # data = parser.parse_args()
        # print(data)
        # print(dict(data))
        # print(type(data))

        data = request.get_json()
        item = next(filter(lambda x: x['name'] == data['name'], items))
        if item is None:
            item = {'name':data['name'],'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return item
        

# get all the items from list
class ItemList(Resource):
    def get(self):
        return {'items' : items}


#api.add_resource(Item,'/item/<string:name>') # http://127.0.0.1:5000/student/Supriya
api.add_resource(Item,'/item')

api.add_resource(ItemList,'/items')

# app.run(port=5000) # here, debug is off. it won't show us errors if any
app.run(port=5000, debug=True) # we want to see errors if any, therefore debug=True

