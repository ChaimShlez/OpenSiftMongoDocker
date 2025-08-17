from pymongo import MongoClient
import os

class ConnectionWrapper:
    def __init__(self):

        self.client = MongoClient(
            host=os.getenv("MONGODB_HOST"),
            port=int(os.getenv("MONGODB_PORT", )),
            username=os.getenv("MONGODB_USER"),
            password=os.getenv("MONGODB_PASSWORD"),
            authSource=os.getenv("MONGODB_DATABASE")
        )
        self.db = self.client[os.getenv("MONGODB_DATABASE")]

    def get_all(self, collection_name):

        try:
            collection = self.db[collection_name]
            return list(collection.find({}))
        except Exception as e:
            print(f"MongoDB get_all error: {e}")
            return []
