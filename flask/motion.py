import pymongo
import json
from bson import ObjectId
import pandas as pd
import numpy as np
import joblib

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["iot"]
mycol = mydb["motion"]

def add_one(new_document):
    mycol.insert_one(new_document)

def retrieve_all():
    cursor = mycol.find({})
    fields_to_include = ['motion', "timestamp"]
    cursor_list = [bson_to_string(doc) for doc in cursor]
    filtered_cursor_list = [{key: doc[key] for key in fields_to_include} for doc in cursor_list]
    # cursor_json = json.dumps(cursor_list) # display all fields
    cursor_json = json.dumps(filtered_cursor_list)
    return cursor_json

def retrieve_latest():
    cursor = mycol.find_one(sort=[('_id', pymongo.DESCENDING)])
    fields_to_include = ['motion', 'timestamp']
    filtered_document = {key: cursor[key] for key in fields_to_include}
    document_json = json.dumps(filtered_document)
    return json.loads(document_json)

def retrieve_latest_50():
    document_count = mycol.count_documents({})
    if document_count >= 50:
        cursor = mycol.find().sort([('_id', pymongo.DESCENDING)]).limit(50)
        motion_values = [doc['motion'] for doc in cursor] 
        df = pd.DataFrame(columns=[f'motion{i+1}' for i in range(50)])
        df.loc[0] = motion_values
        clf_loaded = joblib.load('motion_model.pkl')
        predictions = clf_loaded.predict(df)
        print("\nPredictions for the dummy data:")
        sleep = 0
        for pred in enumerate(predictions):
            if pred == 1:
                sleep = 1
                print(1)
            else:
                sleep = 0
                print(0)
        return sleep
    else:
        print('None')
        return None

def bson_to_string(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    elif isinstance(obj, dict):
        return {key: bson_to_string(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [bson_to_string(item) for item in obj]
    return obj

# def add_many(new_list):
#     mycol.insert_many(new_list)

#     cursor = mycol.find({})
#     for document in cursor:
#         print(document)

# def del_all():
#     x = mycol.delete_many({})
#     print(x.deleted_count, " documents deleted.")

# def del_one(del_document):
#     mycol.delete_one(del_document)


# def update_doc(old_values, new_values):
#     mycol.update_one(old_values, { "$set": new_values })
#     cursor = mycol.find({})
#     for document in cursor:
#         print(document)


retrieve_latest_50()