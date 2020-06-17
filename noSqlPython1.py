import pymongo
from pymongo import MongoClient
print("Enter input  here")
aa = input("Input Please:")
# Creating Database
myclient = MongoClient('localhost',27017)
mydb = myclient["dammyDatabase"]
# this will provide a list of databases
print(myclient.list_database_names())
# this will check if database is exist or not
dblist = myclient.list_database_names()
if "dammyDatabase" in dblist:
    print("Database exist")
else:
    print("Database not exist")
# Creating collection
collection = mydb[aa]
print(mydb.list_collection_names())
collist = mydb.list_collection_names()
if "forum" in collist:
    print("Collection exist")
else:
    print("Collection not exist")

mydict = { "name": "John", "address": "Highway 37" }
x = collection.insert_one(mydict)
print(x.inserted_id)
print("..........done")