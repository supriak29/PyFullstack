import json
from flask import Flask, jsonify, request

app = Flask(__name__)


stores = [   # list
    {    # dictionary
        'name':'DMart',
        'items':[
            {
                'name':'Tooth Brush',
                'price': 25
            },
            {
                'name': 'Shampoo',
                'price': 350
            },
            {
                'name': 'Biscuits',
                'price': 90
            }
        ]
    },
    {
        'name':'Big Bazzar',
        'items':[
            {
                'name': 'Milk',
                'price': 25
            },
            {
                'name': 'Tea Powder',
                'price': 120
            },
            {
                'name': 'Oil',
                'price': 300
            }
        ]
    }
]





# GET / stores  gives details of all stores
@app.route('/stores')
def getStores():
    #return stores  # returns in json by default 
    return jsonify({'stores': stores}) # converting dictionary into json

# GET / store<string:name>   gives details of single store (getting single store details)
@app.route('/store/<string:name>')  # http//127.0.0.1:5000/store/dmart
def getStore(name):
    print("Requested name of store: ",name)
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'Store not found'})


# POST / store data:{name:}
# function to create a store
@app.route('/store',methods=['POST']) # http://127.0.0.1:5000/store
def createStore():
    # requestData is dictionary (it was in json but then converted into dict with the help of .get_json())
    requestData = request.get_json() #get name of store as requested by client (all data sent through request gets assigned to this variable)
    newStore = {    #dictionary - newStore
        'name': requestData['name'],
        'item': [] # empty array
    }
    stores.append(newStore) 
    return jsonify({'stores': stores},{'Count':len(stores)}) # give the output

# POST / store/<string:name>/item{name:,price: }  -------create an item inside a store
@app.route('/store/<string:name>/item',methods=['POST'])
def createStoreItem(name):
    requestData = request.get_json()
    print("This is the incoming request: ",name)
    for store in stores:
        if store['name'] == name:
            newItem = {
                'name':requestData['name'],
                'price':requestData['price']
            }
            store['item'].append(newItem)
            return jsonify(newItem)
    return jsonify({'message': 'Store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def getItemInStore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'Store not found'})

#@app.route('/') # https://127.0.0.1:5000/
#def home():
#    return "This is the first Flask API"

app.run(port=5000) 