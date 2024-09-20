from pymongo import MongoClient

def get_mongo_client():
    client = MongoClient('localhost', 27017)
    return client

def save_to_mongo(collection_name, data):
    if not data:
        print(f"No data to save for collection: {collection_name}")
        return
    client = get_mongo_client()
    db = client['lab_work']
    collection = db[collection_name]
    collection.insert_many(data if isinstance(data, list) else [data])
