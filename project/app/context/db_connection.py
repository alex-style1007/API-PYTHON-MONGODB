import os
from pymongo.mongo_client import MongoClient
from typing import List

class MongoDB():
    client = None

    def __init__(self):
        user = "API" #ELIMINAR
        password = "4321" #ELIMINAR
        cluster_info = "cluster0.3l35xwi.mongodb.net" #ELIMINAR
        # uri = os.environ["uri"] #DESCOMENTAR
        uri = f"mongodb+srv://{user}:{password}@{cluster_info}/?retryWrites=true&w=majority" #ELIMINAR
        self.client = MongoClient(uri, connectTimeoutMS=60000)

    def _get_collection(self, dbname: str, collection: str):
        db = self.client[dbname]
        collection = db[collection]
        return collection