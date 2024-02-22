import pymongo
import pytz
from datetime import datetime
import calendar

# Setup heartrate collection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["heartrate"]

def add_one(new_document):
    mycol.insert_one(new_document)
    cursor = mycol.find({})
    for document in cursor:
        print(document)
# usage: add_one({ "rate": 80, "datetime": datetime_to_epoch() })


def add_many(new_list):
    mylist = [
        { "rate": 80, "datetime": datetime_to_epoch() },
        { "rate": 60, "datetime": datetime_to_epoch() },
        { "rate": 50, "datetime": datetime_to_epoch() },
        { "rate": 80, "datetime": datetime_to_epoch() },
    ]

    mycol.insert_many(new_list)

    cursor = mycol.find({})
    for document in cursor:
        print(document)
# usage: add_many([
    #     { "rate": 80, "datetime": datetime_to_epoch() },
    #     { "rate": 60, "datetime": datetime_to_epoch() },
    #     { "rate": 50, "datetime": datetime_to_epoch() },
    #     { "rate": 80, "datetime": datetime_to_epoch() },
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

def update_doc(old_values, new_values):
    mycol.update_one(old_values, { "$set": new_values })
    cursor = mycol.find({})
    for document in cursor:
        print(document)
# usage: update_doc({ "rate": 80, "datetime": datetime_to_epoch() }, { "rate": 86, "datetime": datetime_to_epoch() })

def process_heartrate():
    hrlist = retrieve_all()
    for hr in hrlist:
        print("Rate: " + str(hr['rate']))
        print("Date Time: " + str(datetime.fromtimestamp(hr['datetime']))) # convert epoch to datetime utc
        if hr['rate'] < 51:
            print("Low Heart rate")
        elif hr['rate'] < 65:
            print("Normal Heart rate")
        elif hr['rate'] < 100:
            print("High Heart rate")
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


process_heartrate()