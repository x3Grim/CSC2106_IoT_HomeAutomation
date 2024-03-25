import pymongo 
import json
from bson import ObjectId
from datetime import datetime

# set up a connection to the database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["seeed_heart_rate"]

# add a document to the collection
def add_one(new_document):
    mycol.insert_one(new_document)
    cursor = mycol.find({})
    for document in cursor:
        print(document)

def add_many(new_list):
    mycol.insert_many(new_list)
    cursor = mycol.find({})
    for document in cursor:
        print(document)

def delete_all():
    x = mycol.delete_many({})
    print(x.deleted_count, " documents deleted.")

def delete_one(document):
    print("Deleted: " + mycol.delete_one(document))

def classify_heart_rate(heart_rate):
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S") 
    if heart_rate >= 40 and heart_rate <= 50:
        return "Sleeping", current_time
    elif heart_rate >= 60 and heart_rate <= 100:
        return "Not Sleeping", current_time
    elif heart_rate < 40:
        return "Very Low", current_time
    else:
        return "Very High", current_time