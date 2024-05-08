import os
from pymongo.mongo_client import MongoClient
from typing import List

class MongoDB():
    client = None

    def __init__(self):
        uri = os.environ["uri"] 
        self.client = MongoClient(uri, connectTimeoutMS=60000)

    def _get_collection(self, dbname: str, collection: str):
        db = self.client[dbname]
        collection = db[collection]
        return collection