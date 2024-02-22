import pymongo
import datetime
import calendar

# Setup pressure collection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["pressure_readings"]

def add_many():
    mylist = [
        { "pressure": 80, "datetime": datetime_to_epoch(2024, 2, 22, 21, 00, 0) },
        { "pressure": 60, "datetime": datetime_to_epoch(2024, 2, 23, 00, 00, 0) },
        { "pressure": 50, "datetime": datetime_to_epoch(2024, 2, 23, 3, 00, 0) },
        { "pressure": 80, "datetime": datetime_to_epoch(2024, 2, 23, 6, 00, 0) },
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

def process_pressure():
    pressureList = retrieve_all()
    for pr in pressureList:
        print("Pressure: " + str(pr['pressure']))
        print("Date Time: " + str(datetime.datetime.fromtimestamp(pr['datetime'])))
        if pr['pressure'] < 0:
            print("Invalid reading")
        elif pr['pressure'] > 100:
            print("User is asleep")
        elif pr['rate'] == 0:
            print("User is dead")

def datetime_to_epoch(year, month, date, hour, minute, second):
    epoch_datetime = datetime.datetime(year, month, date, hour, minute, second)
    return calendar.timegm(epoch_datetime.timetuple())

process_pressure()