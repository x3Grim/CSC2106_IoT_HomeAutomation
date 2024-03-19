import pymongo
import json
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["iot"]
mycol = mydb["pressure"]

def add_one(new_document):
    mycol.insert_one(new_document)

def retrieve_all():
    cursor = mycol.find({})
    fields_to_include = ['pressure']
    cursor_list = [bson_to_string(doc) for doc in cursor]
    filtered_cursor_list = [{key: doc[key] for key in fields_to_include} for doc in cursor_list]
    # cursor_json = json.dumps(cursor_list) # display all fields
    cursor_json = json.dumps(filtered_cursor_list)
    return cursor_json

def retrieve_latest():
    cursor = mycol.find_one(sort=[('_id', pymongo.DESCENDING)])
    fields_to_include = ['pressure', 'timestamp']
    filtered_document = {key: cursor[key] for key in fields_to_include}
    document_json = json.dumps(filtered_document)
    return json.loads(document_json)

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