"""
    This items.py file performs CRUD operations.
    CRUD:   Create - post method, 
            Retrieve - get method, 
            Update - put method, 
            Delete - delete method.
"""

from dbConfig import DatabaseConfig
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from modules.items import ItemModule


# items = []

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help='This field is required'
    )

    parser.add_argument(
        'price',
        type=float,
        required=False,
        help='This field is required'
    )

    # check if the single item is present and return if present
    @jwt_required()
    def get(self):
        data = Item.parser.parse_args()
        item = ItemModule.findItem(data['name'])
        if item:
            return item.json()
        return {'message': 'Item not found1'}, 404

        # data = request.get_json()
#         item = next( filter(lambda x: x['name']==data['name'], items), None)
#         return {'item':item}, 200 if item else 404
# ##        for item in items:
##            if item['name'] == name:
##                return item
##       return {'item': 'No item in the store'}, 404 # status 404 - error
   
    @classmethod
    def findItem(cls, name):
        connection, cursor = DatabaseConfig('data').createConnection()
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return{ "item":{
                'name': row[0],
                'price': row[1]   
            }}
    
    @classmethod
    def insert(cls,item):
        connection, cursor = DatabaseConfig('data').createConnection()
        query = "INSERT INTO  items VALUES(?, ?)" 
        cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()

    @classmethod
    def update(cls,item):
        connection, cursor = DatabaseConfig('data').createConnection()
        query = "UPDATE items SET price=? WHERE name=?" 
        cursor.execute(query, (item['price'], item['name']))
        connection.commit()
        connection.close()


    @jwt_required()
    def post(self):
        data = Item.parser.parse_args()

        if ItemModule.findItem(data['name']):
            return {'message':"An item with name '{}' already exists.".format(data['name'])}, 400
        
        # creating an object: item
        item = ItemModule(name:data['name'], price:data['price'])
        
        try:
            # calling the class method insert
            # ItemModule.insert(item)
            item.insert()
        except:
            return{"message": "An error occurred while inserting item"}, 500
        return item, 201

    # # create an item, insert into list of items and return list of all items
    # def post(self):
    #     data = request.get_json() # json gets converted into dictionary
    #     if next(filter(lambda x: x['name']== data['name'], items), None):
    #         return {'message':"An item with name '{}' already exists.".format(data['name'])}, 400
    #     else:
    #         # print(data)
    #         item = {'name':data['name'],'price':data['price']}
    #         #item = {'name':name,'price':12.00} # static
    #         items.append(item)
    #         return items, 201 # status 201, creating something


    @jwt_required()
    def delete(self):
        connection, cursor = DatabaseConfig('data').createConnection()
        data =  Item.parser.parse_args()
        
        if ItemModule.findItem(data['name']):
            query = "DELETE FROM items WHERE name=?"
            cursor.execute(query, (data['name'],))
            connection.commit()
            connection.close()
            return {"message": "Item Removed from database"}
        return {"message": "Item does not exist in the database"}

        # # trying to access global variable in local scope
        # # global items
        # data = request.get_json() # taking input from user
        # items = list(filter(lambda x: x['name'] != data['name'], items))
        # return {'message':'Item deleted'}
    
    # update list
    @jwt_required()
    def put(self):
        data =  Item.parser.parse_args()
        item = ItemModule.findItem(data['name'])
        updatedItem = ItemModule(name=data['name'], price=data['price'])
        
        if item is None:
            try:
                updatedItem.insert(updatedItem)
                return {"message": "Database updated"}
            except:
                return{"message": "An error occurred while inserting item"}, 500
        else:
            try:
                updatedItem.update(updatedItem)
                return {"message": "Database updated"}
            except:
                return{"message": "An error occurred while inserting item"}, 500
        return updatedItem.json()
            
            # query = "INSERT INTO  items VALUES(?, ?)" 
            # cursor.execute(query, (item['name'], item['price']))
            # connection.commit()
            # connection.close()
            # return {"message": "Database updated"}
        
        # add item into database

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

        # data = request.get_json()
        # item = next(filter(lambda x: x['name'] == data['name'], items))
        # if item is None:
        #     item = {'name':data['name'],'price':data['price']}
        #     items.append(item)
        # else:
        #     item.update(data)
        # return item
        

# get all the items from list
class ItemList(Resource):
  
    def get(self):
        connection, cursor = DatabaseConfig('data').createConnection()
        
        query = "SELECT * FROM items"
        result = cursor.execute(query)
    
        items = []
        for row in result:
            items.append({'name':row[0], 'price':row[1]})

        connection.close()
        return {'items': items}
        # if row:
        #     return{ "item":{
        #         'name': row[0],
        #         'price': row[1]   
        #     }}