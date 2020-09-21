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

  def filter(self, id):
    return ({ "_id": ObjectId(id) })

  def body(self, book):
    return json.loads(book.decode('utf-8'))

  def GetAll(self):
    result = self.books.find()
    return dumps(result, indent=2)

  def PostOne(self, book):
    result = self.books.insert_one(self.body(book))
    return self.GetOne(result.inserted_id)

  def DeleteAll(self):
    res = self.books.delete_many({})
    return res.raw_result

  def GetOne(self, id):
    result = self.books.find_one(self.filter(id))
    return dumps(result, indent=2)

  def PutOne(self, id, book):
    update = { '$set': self.body(book) }
    result = self.books.update_one(self.filter(id), update)
    return result.raw_result

  def DeleteOne(self, id):
    result = self.books.delete_one(self.filter(id))
    return result.raw_result
