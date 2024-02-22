import pymongo
import pytz
from datetime import datetime
import calendar

# Setup pressure collection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["pressure_readings"]

def add_one(new_document):
    mycol.insert_one(new_document)
    cursor = mycol.find({})
    for document in cursor:
        print(document)
# usage: add_one({ "pressure": 80, "datetime": datetime_to_epoch() })


def add_many(new_list):
    mycol.insert_many(new_list)

    cursor = mycol.find({})
    for document in cursor:
        print(document)
# usage: add_many([
    #     { "pressure": 0, "datetime": datetime_to_epoch() },
    #     { "pressure": 50, "datetime": datetime_to_epoch() },
    #     { "pressure": 75, "datetime": datetime_to_epoch() },
    #     { "pressure": 100, "datetime": datetime_to_epoch() },
    # ])

def del_all():
    x = mycol.delete_many({})
    print(x.deleted_count, " documents deleted.")
# deletes all documents

def del_one(del_document):
    mycol.delete_one(del_document)


def retrieve_all():
    cursor = mycol.find({})
    return cursor
# returns list of documents, still need to loop

def retrieve_latest():
    latest_document = mycol.find_one(sort=[('_id', pymongo.DESCENDING)])
    print(latest_document)

def update_doc(old_values, new_values):
    mycol.update_one(old_values, { "$set": new_values })
    cursor = mycol.find({})
    for document in cursor:
        print(document)
# usage: update_doc({ "pressure": 100, "datetime": datetime_to_epoch() }, { "pressure": 0, "datetime": datetime_to_epoch() })

def process_pressure():
    pressure_list = retrieve_all()
    for pressure in pressure_list:
        print(pressure['_id'])
        print("Pressure: " + str(pressure['pressure']))
        print("Date Time: " + str(datetime.fromtimestamp(pressure['datetime']))) # convert epoch to datetime utc
        if pressure['pressure'] < 0:
            print("Invalid pressure value")
        elif pressure['pressure'] > 0:
            print("User is on the bed")
        elif pressure['pressure'] > 250:
            print("User has fallen asleep")
# for processing retrieved data

def datetime_to_epoch():
    utc_now = datetime.utcnow()
    utc_timezone = pytz.timezone('UTC')
    utc_now = utc_timezone.localize(utc_now)
    sg_timezone = pytz.timezone('Asia/Singapore')
    sg_now = utc_now.astimezone(sg_timezone)
    epoch_time = calendar.timegm(sg_now.utctimetuple())
    return epoch_time
# convert current time to epoch

retrieve_latest()