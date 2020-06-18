import pymongo
import datetime
from pymongo import MongoClient


client = MongoClient()
client = MongoClient('localhost',27017)
db = client.dammyDatabase
collection = db['forum']
post = {
      "author": "Mike",
      "text": "My first blog post!",
     "tags": ["mongodb", "python", "pymongo"],
     "date": datetime.datetime.utcnow()}
posts = db.posts
posts.insert_one(post)
print("done")