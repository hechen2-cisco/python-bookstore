#!/usr/local/bin/python3

from flask import Flask, request
from flask_cors import CORS
from dba import Books

app = Flask(__name__)
CORS(app)
books = Books()

@app.route("/")
def hello():
  return "Hello, World!"

@app.route('/books', methods=['GET', 'POST', 'DELETE'])
def doBooks():
  if request.method == 'GET':
    return books.doGetBooks()
  elif request.method == 'POST':
    result = books.doPostBooks(request.data)
    if result:
      return result, 201
    else:
      return { 'message', 'post error'}, 500
  elif request.method == 'DELETE':
    return books.doDeleteBooks(), 204
  else:
    return books.doNoBook(), 404

@app.route('/book/<id>', methods=['GET', 'PUT', 'DELETE'])
def doBook(id):
  print('id:', id)
  if request.method == 'GET':
    result = books.doGetBook(id)
    if result != 'null':
      return result, 200
    else:
      return "book not found", 404
  elif request.method == 'PUT':
    return books.doPutBook(id, request.data)
  elif request.method == 'DELETE':
    return books.doDeleteBook(id), 204
  else:
    return books.doNoBook(), 404

if __name__ == '__main__':
  app.run(debug=True)
