from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required


from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'supriya'
api = Api(app)


jwt = JWT(app, authenticate, identity)

books = []

class Book(Resource):
    def get(self):
        data = request.get_json()
        book = next( filter(lambda x: x['title']==data['title'], books), None)
        return {'book':book}, 200 if book else 404

    def post(self):
        data = request.get_json() # json gets converted into dictionary
        if next(filter(lambda x: x['title']== data['title'], books), None):
            return {'message':"Book with name '{}' already exists.".format(data['title'])}, 400
        else:
            book = {'title':data['title'],'author':data['author'], 'cover':data['cover'],'used':data['used'],'price':data['price'],'discount':data['discount'],'shipping':data['shipping'],'returnable':data['returnable']}
            books.append(book)
            return books, 201 # status 201, creating something

    def delete(self):
        # trying to access global variable in local scope
        global books
        data = request.get_json()
        books = list(filter(lambda x: x['title'] != data['title'], books))
        return {'message':'Book deleted'}
    
    # update list
    def put(self):
        data = request.get_json()
        book = next(filter(lambda x: x['title'] == data['title'], books))
        if book is None:
            book = {'title':data['title'],'author':data['author'], 'cover':data['cover'],'used':data['used'],'price':data['price'],'discount':data['discount'],'shipping':data['shipping'],'returnable':data['returnable']}
            books.append(book)
        else:
            book.update(data)
        return book
        

# get all the items from list
class BookList(Resource):
    def get(self):
        return {'books' : books}


api.add_resource(Book,'/book')
api.add_resource(BookList,'/books')

app.run(port=5000, debug=True)

