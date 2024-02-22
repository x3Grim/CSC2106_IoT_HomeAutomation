import pymongo
from datetime import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["pressure_readings"]

datetime_now = datetime.utcnow()
formatted_date = datetime_now.strftime("%Y-%m-%d %H:%M:%S")

mydict = {
    "date": formatted_date,
    "pressure": "testing"
    }

insertOne = mycol.insert_one(mydict)
findOne = mycol.find_one()

print(myclient.list_database_names())
print(mydb.list_collection_names())
for data in mycol.find():
  print(data)
