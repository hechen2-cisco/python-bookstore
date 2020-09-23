#!/usr/local/bin/python

from flask import Flask, request
from flask_cors import CORS
from dba import Books

app = Flask(__name__)
CORS(app)
books = Books()

@app.route("/")
def hello():
  return "Hello, World!"

@app.route('/books', methods=['GET'])
def GetAllBooks():
  return books.GetAll()

@app.route('/books', methods=['POST'])
def PostOneBook():
  result = books.PostOne(request.data)
  if result:
    return result, 201
  else:
    return { 'message', 'post error'}, 500

@app.route('/books', methods=['DELETE'])
def DeleteAllBooks():
  return books.DeleteAll(), 204

@app.route('/book/<id>', methods=['GET'])
def GetOneBook(id):
  result = books.GetOne(id)
  if result != 'null':
    return result, 200
  else:
    return "book not found", 404

@app.route('/book/<id>', methods=['PUT'])
def PutOneBook(id):
  return books.PutOne(id, request.data)

@app.route('/book/<id>', methods=['DELETE'])
def DeleteOneBook(id):
  return books.DeleteOne(id), 204

if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0') # must have `host` setting!
