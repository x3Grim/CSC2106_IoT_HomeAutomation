import pymongo
import datetime
import calendar

# Setup heartrate collection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["heartrate"]

def add_many():
    mylist = [
        { "rate": 80, "datetime": datetime_to_epoch(2024, 2, 22, 21, 00, 0) },
        { "rate": 60, "datetime": datetime_to_epoch(2024, 2, 23, 00, 00, 0) },
        { "rate": 50, "datetime": datetime_to_epoch(2024, 2, 23, 3, 00, 0) },
        { "rate": 80, "datetime": datetime_to_epoch(2024, 2, 23, 6, 00, 0) },
    ]

    mycol.insert_many(mylist)

    cursor = mycol.find({})
    for document in cursor:
        print(document)

def del_all():
    x = mycol.delete_many({})
    print(x.deleted_count, " documents deleted.") 

def retrieve_all():
    cursor = mycol.find({})
    return cursor

def update_doc(old_values, new_values):
    mycol.update_one(old_values, { "$set": new_values })
    cursor = mycol.find({})
    for document in cursor:
        print(document)

def process_heartrate():
    hrlist = retrieve_all()
    for hr in hrlist:
        print("Rate: " + str(hr['rate']))
        print("Date Time: " + str(datetime.datetime.fromtimestamp(hr['datetime'])))
        if hr['rate'] < 51:
            print("Low Heart rate")
        elif hr['rate'] < 65:
            print("Normal Heart rate")
        elif hr['rate'] < 100:
            print("High Heart rate")

def datetime_to_epoch(year, month, date, hour, minute, second):
    epoch_datetime = datetime.datetime(year, month, date, hour, minute, second)
    return calendar.timegm(epoch_datetime.timetuple())


process_heartrate()