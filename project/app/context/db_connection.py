from pymongo.mongo_client import MongoClient
from typing import List

class MongoDB():
    client = None

    def __init__(self):
        user = "API"
        password = "4321"
        cluster_info = "cluster0.3l35xwi.mongodb.net"
        uri = f"mongodb+srv://{user}:{password}@{cluster_info}/?retryWrites=true&w=majority"
        self.client = MongoClient(uri)

    def _get_collection(self, dbname: str, collection: str):
        db = self.client[dbname]
        collection = db[collection]
        return collection