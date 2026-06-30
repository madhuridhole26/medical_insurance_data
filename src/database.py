import pymongo
import config

mongo_client=pymongo.MongoClient(config.MONGO_CLIENT)
db=mongo_client[config.mongo_db]

def get_data_collection():
    data_collection=db[config.data_collection_name]
    return data_collection