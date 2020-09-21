#!/usr/local/bin/python3

from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import json

class Books:
  def __init__(self):
    client = MongoClient('mongodb://localhost:27017')

    db = client['bookstore']
    self.books = db['books']

  def doGetBooks(self):
    cursor = self.books.find()
    return dumps(cursor, indent=2)

  def doPostBooks(self, book):
    payload = json.loads(book.decode('utf-8'))
    res = self.books.insert_one(payload)
    print('return id:', res.inserted_id)
    return self.doGetBook(res.inserted_id)

  def doDeleteBooks(self):
    res = self.books.delete_many({})
    return res.raw_result

  def doNoBook(self):
    return {'message', "Content not found"}

  def doGetBook(self, id):
    print('query:', self.query(id))
    result = self.books.find_one(self.query(id))
    print('result:', result)
    return dumps(result, indent=2)

  def doPutBook(self, id, book):
    payload = json.loads(book.decode('utf-8'))
    update = { '$set': payload }
    print('put payload', update)
    res = self.books.update_one(self.query(id), update)
    print ('put result', res)
    return res.raw_result

  def doDeleteBook(self, id):
    res = self.books.delete_one(self.query(id))
    print('deleted a book', res)
    return res.raw_result

  def query(self, id):
    return ({ "_id": ObjectId(id) })